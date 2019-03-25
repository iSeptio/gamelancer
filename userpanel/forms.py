from django import forms
from django.contrib.auth import get_user_model


class profileForm(forms.ModelForm):
    """Form to add profile picture to User model."""

    class Meta:
        """Meta class for profilepictureForm."""

        model = get_user_model()
        fields = ('name', 'profile_pic')
