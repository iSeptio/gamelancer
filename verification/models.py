from django.conf import settings
from django.db import models


class Document(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,)
    passport = models.ImageField()
    id_license = models.ImageField()
