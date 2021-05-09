"""nls_world_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
from django.urls import re_path
from django.views.static import serve

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(
    url='/static/favicon/nls-logo2.ico', permanent=True)

# WITH TRANSLATIONS
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path(_('Site-BackEnd/'), admin.site.urls),
    path('', include('map_app.urls')),
    path('cart/', include('cart.urls')),
    path('members/', include('members.urls')),
    path('favicon.ico/', favicon_view),
    prefix_default_language=False,

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

handler404 = 'map_app.views.error_404_view'
handler500 = 'map_app.views.error_500_view'

# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
