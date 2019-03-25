from django.urls import path
from . import views

app_name = 'verification'
urlpatterns = [
    path('', views.upload_document, name='upload')
]
