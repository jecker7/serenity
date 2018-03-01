from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required = False, help_text='(optional)')
    last_name = forms.CharField(max_length=30, required = False, help_text='(optional)')
    email = forms.EmailField(max_length = 214, required = False, help_text = '(optional)')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    #password password_validation
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password2']  != cd['password']:
            raise ValidationError("passwords don't match")
        return cd['password']
