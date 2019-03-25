from django.urls import path
from . import views

app_name = 'userpanel'
urlpatterns = [
    path('', views.index, name='index'),
    path('settings/profile_settings/',
         views.profile_settings, name='profilesettings'),
]
