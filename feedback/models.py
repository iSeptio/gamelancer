from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class FeedbackQuerySet(models.QuerySet):
    def feedback_ratio(self, user_id):
        negative = self.filter(feedback=-1, recipient_id=user_id).count()
        neutral = self.filter(feedback=0, recipient_id=user_id).count()
        positive = self.filter(feedback=1, recipient_id=user_id).count()
        return ((positive-negative)+neutral+1)/(positive+negative+neutral+1)*100


class FeedbackManager(models.Manager):
    def get_queryset(self):
        return FeedbackQuerySet(self.model, using=self._db)

    def for_userid(self, user_id):
        return self.get_queryset().feedback_ratio(user_id)


class FeedbackModel(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipient')
    FEEDBACK_OPTION = (
        (-1, 'Negative'),
        (0, 'Neutral'),
        (+1, 'Good'),
    )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    feedback = models.IntegerField(choices=FEEDBACK_OPTION)
    opinion = models.CharField(max_length=255)
    objects = models.Manager()
    manager = FeedbackManager()


class Meta:
    ordering = ['recipient', '-sender']
