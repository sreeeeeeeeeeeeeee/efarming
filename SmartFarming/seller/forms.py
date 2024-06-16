from django import forms
from django.forms import ModelForm
from .models import *
from farmadmin.models import *
from farmer.models import *
import re
class sellerForms(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=sellerregister
        fields=[
            'ownername',
            'phoneno',
            'address',
            'shopname',
            'location',
            'email',
            'password'

        ]
        
        labels={
            'ownername':'Enter your name',
            'phoneno':'Phone Number',
            'address':'Address',
            'shopname':'Shop name',
            'location':'Location',
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
    
class sellingProductForms(forms.ModelForm):
    class Meta:
        model=sellingProducts
        fields=[
            'pname',
            'pimage',
            'pcategory',
            'description',
            'price',
            'status'
        ]
        
        labels={
            'pname':'Product Name',
            'pimage':'Image',
            'pcategory':'Category',
            'description':'Description',
            'price':'Price per item',
            'status':'Status'
        }

class updatetoolForms(forms.ModelForm):
    class Meta:
        model=sellingProducts
        fields=[
            'pname',
            'pimage',
            'description',
            'price',
            'status'
        ]
        
        labels={
            'pname':'Product Name',
            'pimage':'Image',
            'description':'Description',
            'price':'Price per item',
            'status':'Status'
        }

class editsellerForms(forms.ModelForm):
    class Meta:
        model=sellerregister
        fields=[
            'ownername',
            'phoneno',
            'address',
            'shopname',
            'location',
            'email',

        ]
        
        labels={
            'ownername':'Enter your name',
            'phoneno':'Phone Number',
            'address':'Address',
            'shopname':'Shop name',
            'location':'Location',
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

class rentToolForms(forms.ModelForm):
    class Meta:
        model=rentTools
        fields=[
            'tname',
            'timage',
            'description',
            'priceperday',
            'nooftools',
            'status'
        ]
        
        labels={
            'tname':'Tool Name',
            'timage':'Image',
            'description':'Description',
            'priceperday':'Price per day',
            'nooftools':'Number of tools',
            'status':'Status'
        }
class updaterentToolForms(forms.ModelForm):
    class Meta:
        model=rentTools
        fields=[
            'tname',
            'timage',
            'description',
            'priceperday',
            'nooftools',
            'status'
        ]
        
        labels={
            'tname':'Tool Name',
            'timage':'Image',
            'description':'Description',
            'priceperday':'Price per day',
            'nooftools':'Number of tools',
            'status':'Status'
        }

class productRequestForms(forms.ModelForm):
    class Meta:
        model=sendproductRequest
        fields=[
            'product',
            'usertype',
            'quantity',
            'phoneno'
        ]


        labels={
            'product':'Product Id',
            'usertype':'Usertype',
            'quantity':'Quantity',
            'phoneno':'Contact number'
        }
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['product'].empty_label="Select" 