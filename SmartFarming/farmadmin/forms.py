from django import forms
from django.forms import ModelForm
from .models import *
import re
class loginForms(forms.ModelForm):
    class Meta:
        model=login
        fields=[
            'email',
            'password'
        ]
        labels={
            'email':'Enter your email',
            'password':'Enter your password'

        }

class customerForms(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=customerdetails
        fields=[
            'cname',
            'email',
            'phoneno',
            'address',
            'password',
        ]
        labels={
            'cname':'Enter your name',
            'email':'Enter your email',
            'phoneno':'Enter your contact number',
            'address':'Address for communication',
            'password':'Create password',

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

class customerProductOrderRequestForms(forms.ModelForm):
    class Meta:
        model=customerproductorder
        fields=[
            'product',
            'quantity',
            'address',
            'contactno',
            

        ]
        labels={
            'product':'Product',
            'quantity':'Quantity',
            'address':'Address',
            'contactno':'Contact No',
        }
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['product'].empty_label="Select"


class customerMachineryOrderRequestForms(forms.ModelForm):
    class Meta:
        model=customermachineryorder
        fields=[
            'product',
            'quantity',
            'pcategory',
            'address',
            'contactno',
            

        ]
        labels={
            'product':'Product',
            'quantity':'Quantity',
            'pcategory':'Category',
            'address':'Address',
            'contactno':'Contact No',
        }
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['product'].empty_label="Select"

class editcustomerForms(forms.ModelForm):
    class Meta:
        model=customerdetails
        fields=[
            'cname',
            'email',
            'phoneno',
            'address',
        ]
        labels={
            'cname':'Enter your name',
            'email':'Enter your email',
            'phoneno':'Enter your contact number',
            'address':'Address for communication',

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
