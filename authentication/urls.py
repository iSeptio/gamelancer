from django.urls import path, re_path, include
from . import views
from django.conf.urls import url


app_name = 'authentication'
urlpatterns = [
    path('login', views.logmein, name='login'),
    path('logout', views.logmeout, name='logout'),
    path('signup', views.signup, name='signup'),
    re_path(r'^account_activation_sent/$', views.account_activation_sent,
            name='account_activation_sent'),
    re_path(
        r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'
    ),


]
