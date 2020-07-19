from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Address, Member

class MemberUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ['first_name','last_name']