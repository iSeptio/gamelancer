"""epicnpc2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # starting language paths with predefined prefixes
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(

    path(_('authentication/'),
         include('authentication.urls', namespace='authentication')),
    path(_('feedback/'),
         include('feedback.urls', namespace='feedback')),
    path(_('admin/'), admin.site.urls),
    path((''), include('userpanel.urls', namespace='userpanel')),
    path(_('verification/'), include('verification.urls', namespace='verification')),
    path("api/", include("simple-feedback.urls")),
    prefix_default_language=True,
)

# urlpatterns += staticfiles_urlpatterns()  # not sure if works
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)  # not sure if works
