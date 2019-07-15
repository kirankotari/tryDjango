from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '193.113.42.151']

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')


INSTALLED_APPS += [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'debug_toolbar',
    'core',
    'crispy_forms',
    'pages',
    'dashboard'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS


DEBUG_TOOLBAR_PANELS = ['debug_toolbar.panels.versions.VersionsPanel', 'debug_toolbar.panels.timer.TimerPanel', 'debug_toolbar.panels.settings.SettingsPanel',
                        'debug_toolbar.panels.headers.HeadersPanel', 'debug_toolbar.panels.request.RequestPanel', 'debug_toolbar.panels.sql.SQLPanel',
                        'debug_toolbar.panels.staticfiles.StaticFilesPanel', 'debug_toolbar.panels.templates.TemplatesPanel', 'debug_toolbar.panels.cache.CachePanel',
                        'debug_toolbar.panels.signals.SignalsPanel', 'debug_toolbar.panels.logging.LoggingPanel', 'debug_toolbar.panels.redirects.RedirectsPanel',
                        'debug_toolbar.panels.profiling.ProfilingPanel', ]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, 'SHOW_TOOLBAR_CALLBACK': show_toolbar}

# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), }}

STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/dashboard/'

# ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

ACCOUNT_AUTHENTICATION_METHOD = "username_email"  # ”username” | “email” | “username_email”)
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
# ACCOUNT_EMAIL_CONFIRMATION_HMAC=True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None  # =”optional”
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Employee Skill Management: Signup verification "  # ”[Site] “)
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN=180
# ACCOUNT_EMAIL_MAX_LENGTH=254
# ACCOUNT_FORMS={}
#
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

# ACCOUNT_PRESERVE_USERNAME_CASING=True
# ACCOUNT_SESSION_REMEMBER=None
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE=False
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# ACCOUNT_TEMPLATE_EXTENSION="html"


ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USER_DISPLAY=a callable returning user.username
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USERNAME_VALIDATORS = None
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_FORMS = {
'signup': 'pages.forms.EmployeeSignupForm',
}

# ACCOUNT_USERNAME_VALIDATORS = 'some.module.validators.custom_username_validators'
# SOCIALACCOUNT_ADAPTER (=”allauth.socialaccount.adapter.DefaultSocialAccountAdapter”)
# SOCIALACCOUNT_AUTO_SIGNUP (=True)
# SOCIALACCOUNT_EMAIL_VERIFICATION (=ACCOUNT_EMAIL_VERIFICATION)
# SOCIALACCOUNT_EMAIL_REQUIRED (=ACCOUNT_EMAIL_REQUIRED)
# SOCIALACCOUNT_FORMS (={})
# SOCIALACCOUNT_PROVIDERS (= dict)
# SOCIALACCOUNT_QUERY_EMAIL (=ACCOUNT_EMAIL_REQUIRED)
# SOCIALACCOUNT_STORE_TOKENS (=True)


# add_email: allauth.account.forms.AddEmailForm
# change_password: allauth.account.forms.ChangePasswordForm
# disconnect: allauth.socialaccount.forms.DisconnectForm
# login: allauth.account.forms.LoginForm
# reset_password: allauth.account.forms.ResetPasswordForm
# reset_password_from_key: allauth.account.forms.ResetPasswordKeyForm
# set_password: allauth.account.forms.SetPasswordForm
# signup: allauth.account.forms.SignupForm
# signup: allauth.socialaccount.forms.SignupForm
#
# custom_username_validators = [ASCIIUsernameValidator()]
