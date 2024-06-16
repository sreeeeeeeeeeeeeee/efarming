from django import forms
from django.forms import ModelForm
from .models import *
from farmadmin.models import *
import re
class workerForms(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=workerregister
        fields=[
            'workername',
            'age',
            'gender',
            'phoneno',
            'address',
            'occupation',
            'experience',
            'email',
            'password'

        ]
        
        labels={
            'workername':'Enter your name',
            'age':'Age',
            'gender':'Gender',
            'phoneno':'Phone Number',
            'address':'Address',
            'occupation':'Occupation',
            'experience':'Experience',
            'email':'Email address',
            'password':'Create password'

        }
    def clean_confirm_password(self):
        cpwd = self.cleaned_data.get('confirm_password')
        pwd=self.cleaned_data.get('password')
        if cpwd!=pwd:
           raise forms.ValidationError('password doesnot matching!') 
        return pwd
    def clean_email(self):
        email = self.cleaned_data['email']
        if login.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    def clean_mobile(self):
        n=str(self.cleaned_data['phoneno']) 
        r=re.fullmatch('[6-9][0-9]{9}',n)
        mob=self.cleaned_data['phoneno'] 
        if r==None: 
            raise forms.ValidationError('Enter Valid Phone number!')
        return mob
    
class editworkerForms(forms.ModelForm):
    class Meta:
        model=workerregister
        fields=[
            'workername',
            'age',
            'gender',
            'phoneno',
            'address',
            'occupation',
            'experience',
            'email',

        ]
        
        labels={
            'workername':'Enter your name',
            'age':'Age',
            'gender':'Gender',
            'phoneno':'Phone Number',
            'address':'Address',
            'occupation':'Occupation',
            'experience':'Experience',
            'email':'Email address',

        }
    def clean_email(self):
        email = self.cleaned_data['email']
        if login.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    def clean_mobile(self):
        n=str(self.cleaned_data['phoneno']) 
        r=re.fullmatch('[6-9][0-9]{9}',n)
        mob=self.cleaned_data['phoneno'] 
        if r==None: 
            raise forms.ValidationError('Enter Valid Phone number!')
        return mob