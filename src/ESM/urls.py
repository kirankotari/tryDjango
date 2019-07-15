from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, content_view, social_view, about_view, userProfile

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', content_view, name='contact'),
    path('about/', about_view, name='about'),
    path('profile/', userProfile, name='profile'),
    path('social/', social_view, name='social'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
