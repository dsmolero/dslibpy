dslibpy.views.restricted
========================
DJANGO CLASS-BASED-VIEWS WITH OBJECT-LEVEL PERMISSIONS CHECKING
---------------------------------------------------------------
##### Darwinian Software Library for Python
Author: [Darwin Molero](http://blog.darwiniansoftware.com/about)

Description
-----------
No need for `@login_required` and `@permission_required` decorators. These
reusable Django class-based-views will provide object-level permissions to its
subclasses more than what those two can offer. These views take a step ahead by
giving an option to make views accessible only to the owner of the object (via
the usual model attributes `.user`, `.owner`, or `.creator`).

Classes
-------
1. RestrictedCreateView
        - subclass of django.views.generic.CreateView
2. RestrictedDetailView
        - subclass of django.views.generic.DetailView
3. RestrictedListView
        - subclass of django.views.generic.ListView
4. RestrictedUpdateView
        - subclass of django.views.generic.UpdateView
5. RestrictedDeleteView
        - subclass of django.views.generic.DeleteView
6. RestrictedMixin
        - for use with views that inherit from other classes

Usage
-----
### .restriction attribute

There are 8 restriction levels that you can assign to your class-based-views:

* 0 - Nobody has access (not even you? aw!)
* 1 - Only super users have access.
* 2 - Any staff with permissions has access.
* 3 - The owner of the object has access (request.user == object.user,
      object.owner, etc.)
* 4 - Any logged-in user with model-level permissions has access.
* 5 - Any staff has access (request.user.is_staff == True).
* 6 - Any logged-in user has access (request.user.is_authenticated() == True).
* 7 - Anybody have access.

You set the restriction through the `restriction` attribute of the view class.
This attribute is an integer (not string).

For example:

    class MyClass(RestrictedDeleteView):
        model = Blog
        restriction = 1

will only allow superusers (admins) to delete Blog objects.

The restrictions filter-through, meaning a user is evaluated from the top
(level 1) downwards until the user qualifies on a level which grants him/her
access. When a user fails to pass the restriction level set for the view, a
`PermissionDenied()` exception is thrown.

### .owner_field attribute

For models in which objects belong to a user (i.e. owned by a user).
set the `owner_field` attribute to the name of the field that is a ForeignKey
to `django.contrib.auth.models.User`. This attribute is a string. It is
mainly used to views that have `restriction = 3`.

You do not have to declare an `owner_field` attribute if you don't need
restriction level 3. It will simply be ignored in other restriction levels.

For example:

    #models.py--------------------------------------------

    from django.db import models
    from django.contrib.auth.models import User

    class Blog(models.Model):
        title = models.CharField(max_length=255)
        user = models.ForeignKey(User)


    #views.py----------------------------------------------

    from dslibpy.views.restricted import RestrictedUpdateView
    from myproject.blogs.forms import BlogModelForm

    class BlogRestrictedUpdateView(RestrictedUpdateView):
        model = Blog
        form_class = BlogModelForm
        restriction = 3

will grant access to the owner of the Blog object (level 3). It will also
grant access to any staff (is_staff == True) provided that they have
"change" permission for Blog objects (level 2). It will also grant access
to all superusers (level 1).
Users who belong to level 4 and below are NOT granted access to this view.
Note here that the view does not have the `owner_field` attribute. You can also
do this and the view will safely ignore objects that do not have owners in the
first place. To be exact, this view will grant access to levels 1 and 2 users
only although it indicates level 3.

### More Examples
The following usage examples are based on the Blog model above.

### Using RestrictedCreateView

this code:

    from dslibpy.views.restricted import RestrictedCreateView

    class BlogRestrictedCreateView(RestrictedCreateView):
        model = Blog
        owner_field = 'user'
        restriction = 5

will make BlogRestrictedCreateView automatically save the logged-in user
into the field `user` of the Blog object (i.e. object.user == request.user).
Also it grants access not only to the owner and the admins but also to
any authenticated user who is a staff (is_staff == True) and to any
authenticated user who has "add" permissions on the Blog model.

### Using RestrictedDetailView

this code:

    from dslibpy.views.restricted import RestrictedDetailView

    class BlogRestrictedDetailView(RestrictedDetailView):
        model = Blog
        owner_field = "user"
        restriction = 2

will only allow admins, and staff users (is_staff == True) who have "view"
permissions on the Blog model.


### Using RestrictedListView

this code:

    from dslibpy.views.restricted import RestrictedListView

    class BlogRestrictedListView(RestrictedListView):
        model = Blog
        template_name = "blogs/blog_list.html"
        owner_field = 'user'
        restriction = 7

        def get_queryset_perm(self, user):
            queryset = super(StockPositions, self).get_queryset_perm(user)
            # one-million-lines-of-code-here

will allow all users including guests and visitors who are not logged in
to view the list of blog entries.

RestrictedListView deserves special mention here. The default `get_queryset()`
method now is wrapped in `get_queryset_perm()` which requires passing of the
user object (request.user). Aside from that, the usual attributes like
`template_name`, `success_url`, etc. retain their default behaviors.


### Using RestrictedUpdateView

The first example already covered using this view. Please refer to it.

### Using RestrictedDeleteView

I will leave the usage of this view as an exercise for you. Besides, this
documentation has become longer than what I thought.

### Using RestrictedMixin

this code:

    from dslibpy.views.restricted import RestrictedMixin
    from myproject.profiles.views import ProfileUpdateView

    class CustomerProfileUpdateView(RestrictedMixin, ProfileUpdateView):
        model = CustomerProfile
        user = 'customer'
        restriction = 3

    class VendorProfileUpdateView(RestrictedMixin, ProfileUpdateView):
        model = VendorProfile
        user = "vendor"
        restriction = 3

will allow you to have all the security features of `dslibpy.views.restricted`
alongside the reusable features of your existing class-based-views.
Just make sure that `RestrictedMixin` is the first in the list of base
classes so that its methods are called first in the command chain.

<< [Back to Main](../../README.md)
