from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'date_of_birth')
