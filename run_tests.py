__author__ = 'bms'

import sys

from django.conf import settings


def main():
    settings.configure(
        DEBUG=True,
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
        #ROOT_URLCONF='myapp.urls',
        INSTALLED_APPS=(
            # 'django.contrib.auth',
            # 'django.contrib.contenttypes',
            # 'django.contrib.sessions',
            # 'django.contrib.admin',
            'django_forms_bootstrapped',
        ),
        LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'filters': {
                'require_debug_false': {
                    '()': 'django.utils.log.RequireDebugFalse'
                },
            },
            'formatters': {
                'simple': {
                    'format': '%(asctime)s %(levelname)s %(name)s: %(message)s',
                },
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple',
                },
            },
            'loggers': {
                'django_forms_bootstrapped': {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                },
            },
        },
    )
    from django.test.utils import get_runner

    runner = get_runner(settings)(verbosity=2, interactive=True)
    failures = runner.run_tests(['django_forms_bootstrapped'])
    sys.exit(failures)


if __name__ == '__main__':
    main()
