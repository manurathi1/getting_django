from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    """Form definition for UserRegistration."""

    password = forms.CharField(label = 'Password' , widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat Password' , widget = forms.PasswordInput)

    class Meta:
        """Meta definition for UserRegistrationform."""

        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password doesnt match')

        return cd['password2']

            






