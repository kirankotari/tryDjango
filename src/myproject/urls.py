from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, content_view, social_view, about_view

urlpatterns = [
    path('product/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('', home_view, name='home'),
    path('content/', content_view, name='content'),
    path('about/', about_view, name='product-lookup'),
    path('social/', social_view, name='social'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
