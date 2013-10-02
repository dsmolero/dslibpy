"""
dslibpy.views.restricted.py

Django Class-Based-Views with Object-Level Permissions Checking

"""

__author__ = 'Darwin Molero (http://darwiniansoftware.com)'

from django.core import exceptions
from django.core.exceptions import ImproperlyConfigured
from django.utils.text import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect


# The following restrictions flow-through, meaning a user is evaluated from the top (level 1)
# downwards until the user qualifies on a level further down below.
RESTRICTION_LEVELS = {"0": "Nobody has access",     # not even god? oh, well.
                      "1": "Any super user have access.",
                      "2": "Any staff with permissions have access.",
                      "3": "The owner of the object have access.",
                      "4": "Any logged-in user with permissions have access.",
                      "5": "Any staff have access.",
                      "6": "Any logged-in user have access.",
                      "7": "Anybody have access."}
# For example, if a view has restriction 4, then all level 1, 2, 3, and 4 users have access to the view.
# Level 5, 6, 7 users have NO access since they are lower than restriction 4.


class RestrictedMixin(object):
    restriction = 7     # override in subclass as any of: 1, 2, 3, 4, 5, 6, 7
    action = None       # override in subclass as any of:  "add", "change", "delete", "view"
    owner_field = None  # field that foreignKeys to auth.User

    def _has_perm(self, user):
        params = {'app': self.model._meta.app_label,
                  'model': self.model.__name__,
                  'action': self.action}
        rule = "{app}.{action}_{model}".format(**params).lower()
        ret = user.has_perm(rule)
        return ret

    def _is_owner(self, user, obj):
        if bool(obj) and bool(self.owner_field):
            ret = (getattr(obj, self.owner_field) == user)
        else:
            ret = True
        print ".._is_owner == %s" % ret
        return ret

    def _filter_access(self, user, obj=None):
        if self.restriction >= 1 and user.is_superuser:
            print "..passed 1"
            #pass
        elif self.restriction >= 2 and user.is_staff and self._has_perm(user):
            print "..passed 2"
            #pass
        elif self.restriction >= 3 and self._is_owner(user, obj):
            print "..passed 3"
            #pass
        elif self.restriction >= 4 and self._has_perm(user):
            print "..passed 4"
            #pass  # happens in CreateView
        elif self.restriction >= 5 and user.is_staff:
            print "..passed 5"
            #pass
        elif self.restriction >= 6 and user.is_authenticated():
            print "..passed 6"
            #pass
        elif self.restriction >= 7:
            print "..passed 7"
            #pass
        else:
            raise exceptions.PermissionDenied()

    def dispatch(self, request, *args, **kwargs):
        self._filter_access(request.user)
        return super(RestrictedMixin, self).dispatch(request, *args, **kwargs)


class RestrictedListView(RestrictedMixin, ListView):
    action = "list"

    def get_queryset_perm(self, user):
        """
        Get the list of items for this view. This must be an interable, and may
        be a queryset (in which qs-specific behavior will be enabled).
        """
        if self.queryset is not None:
            queryset = self.queryset
            if hasattr(queryset, '_clone'):
                queryset = queryset._clone()
        elif self.model is not None:
            lookup_args = {self.owner_field: user}
            queryset = self.model._default_manager.filter(**lookup_args)
        else:
            raise ImproperlyConfigured(u"'%s' must define 'queryset' or 'model'"
                                       % self.__class__.__name__)
        return queryset

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset_perm(request.user)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)


class RestrictedDetailView(RestrictedMixin, DetailView):
    action = "view"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        print '..'
        self._filter_access(request.user, self.object)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class RestrictedCreateView(RestrictedMixin, CreateView):
    action = "add"

    def _set_owner(self, obj, user):
        """
        Assign the user as owner of the object.
        """
        if self.get('owner_field', None):
            setattr(obj, self.owner_field, user)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self._set_owner(form.instance, request.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RestrictedUpdateView(RestrictedMixin, UpdateView):
    action = "change"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self._filter_access(request.user, self.object)
        return super(RestrictedUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self._filter_access(request.user, self.object)
        return super(RestrictedUpdateView, self).post(request, *args, **kwargs)


class RestrictedDeleteView(RestrictedMixin, DeleteView):
    action = "delete"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self._filter_access(request.user, self.object)
        return super(RestrictedDeleteView, self).get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self._filter_access(request.user, self.object)
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
