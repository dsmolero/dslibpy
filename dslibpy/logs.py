import logging
import os

from django.conf import settings

#
# For Django < 1.4
#
# class RequireDebugFalse(logging.Filter):
#     def filter(self, record):
#         return not settings.DEBUG
#
#
# class RequireDebugTrue(logging.Filter):
#     def filter(self, record):
#         return settings.DEBUG


#
# Logging
# =======
#
#   Saves a lot of typing (or copy/paste)
#
#   Usage:
#       in settings.py:
#           from dslibpy.logs import base_logging
#           LOGGING = base_logging()
#
#   default log file:
#       /var/tmp/dslibpy.log
#
#       override by passing the logfile path as argument
#           ex:  base_logging('/var/tmp/my-project-name.log')
#
#   to check your logging configuration:
#       $ python manage.py shell
#       > from django.conf import settings
#       > settings.LOGGING
#
def base_logging(app_name, log_dir=None):
    if not log_dir:
        log_dir = '/var/tmp'
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(asctime)s [%(levelname)s] (%(name)s.%(funcName)s:%(lineno)d): %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'simple': {
                'format': '[%(levelname)s]: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'filters': {
            # 'special': {
            #     '()': 'project.logging.SpecialFilter',
            #     'foo': 'bar',
            # },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'INFO',
                'filters': ['require_debug_false'],
                'class': 'logging.FileHandler',
                'filename':  os.path.join(log_dir, '%s.log' % app_name),
                'formatter': 'verbose'
            },
            'dba_logfile': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'logging.FileHandler',
                'filename': os.path.join(log_dir, '%s_dba.log' % app_name),
                'formatter': 'verbose'
            },
            'mail_admins': {
                'level': 'ERROR',
                # 'filters': ['special']
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler',
                'formatter': 'verbose'
            }
        },
    }


def pro_logging(app_name, log_dir=None):
    logging = base_logging(app_name, log_dir)
    logging.update({
        'loggers': {
            'django': {
                'handlers': ['file', 'mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            app_name: {
                'handlers': ['file', 'mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    })
    return logging


def dev_logging(app_name):
    logging = base_logging(app_name)
    logging.update({
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True
            },
            app_name: {
                'handlers': ['console'],
                'level': 'DEBUG',
            }
        }
    })
    return logging
