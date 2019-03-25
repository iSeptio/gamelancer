from django import forms


class UploadDocument(forms.Form):

    passport = forms.ImageField()
    id_license = forms.ImageField()
