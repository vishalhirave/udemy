from django import forms
from django.contrib.auth.models import User
from .models import userinfo
class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class userinfoform(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=('sites','profile_pic')