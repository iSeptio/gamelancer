from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('leave_feedback/<str:recipient>/',
         views.leave_feedback.as_view(), name='leavefeedback'),
    path('check_feedback/<str:feeedback_for>/',
         views.check_feedback.as_view(), name='checkfeedback')

]
