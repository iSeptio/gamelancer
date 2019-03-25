from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FeedbackModel
from django.contrib.auth import get_user_model
User = get_user_model()
decorators = [login_required]


@method_decorator(decorators, name='dispatch')
class leave_feedback(CreateView):
    model = FeedbackModel
    fields = ['feedback', 'opinion']
    success_url = '/'
    #template_name = "feedback/leave_feedback.html"

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.recipient = get_object_or_404(
            User, username=self.kwargs['recipient'])
        # here enter another instance to know what user is feedback given to :D
        return super().form_valid(form)


class check_feedback(ListView):

    context_object_name = 'Display feedback'
    template_name = 'feedback/feedback_list.html'
    # implement paginator

    def get_queryset(self):
        self.feedback_for = get_object_or_404(
            User, username=self.kwargs['feeedback_for'])
        return FeedbackModel.objects.filter(recipient=self.feedback_for)
