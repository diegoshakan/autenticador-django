from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets ={
            'username': forms.TextInput(attrs={'max_length': 100}),
            'password': forms.PasswordInput(attrs={'max_length': 100}),
            'email': forms.EmailInput(attrs={'max_length': 100}),
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        