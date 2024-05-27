from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args: Any, **kwargs: Any):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].label = 'Email address'
        self.fields['email'].required = True
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        
        if User.objects.filter(email=email).exists() and len(email) > 254:
            raise forms.ValidationError('Email is in use or too long')
        
        return email
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()