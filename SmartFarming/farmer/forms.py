from django import forms
from django.forms import ModelForm
from .models import *
from farmadmin.models import *
import re
class farmerForms(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=farmerregister
        fields=[
            'farmername',
            'phoneno',
            'address',
            'email',
            'password'
        ]
        
        labels={
            'farmername':'Enter your name',
            'phoneno':'Enter your phone no',
            'address':'Address',
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

class addProductForms(forms.ModelForm):
    class Meta:
        model=addProduct
        fields=[
            'productname',
            'productimage',
            'description',
            'price',
            'status'

        ]
        
        labels={
            'productname':'Product Name',
            'productimage':'Image',
            'description':'Description',
            'price':'Price per Kg',
            'status':'Status'
        }

class updateProductForms(forms.ModelForm):
    class Meta:
        model=addProduct
        fields=[
            'productname',
            'productimage',
            'description',
            'price',
            'status'

        ]
        
        labels={
            'productname':'Product Name',
            'productimage':'Image',
            'description':'Description',
            'price':'Price per Kg',
            'status':'Status'
        }

class jobRequestForms(forms.ModelForm):
    class Meta:
        model=sendJobRequest
        fields=[
            'description',
            'duration',
            'payperday',
            'workerid'

        ]

        labels={
            'description':'Job Description',
            'duration':'Duration',
            'payperday':'Pay / Day',
            'workerid':'Worker',
        }
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['workerid'].empty_label="Select" 

class toolOrderRequestForms(forms.ModelForm):
    class Meta:
        model=sendToolOrderRequest
        fields=[
            'usertype',
            'toolid',
            'quantity'
        ]


        labels={
            'usertype':'Usertype',
            'toolid':'Tool Id',
            'quantity':'Quantity',
        }
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['toolid'].empty_label="Select" 

class editprofileForms(forms.ModelForm):
    class Meta:
        model=farmerregister
        fields=[
            'farmername',
            'phoneno',
            'address',
            'email',
        ]
        
        labels={
            'farmername':'Enter your name',
            'phoneno':'Enter your phone no',
            'address':'Address',
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

class rentRequestForms(forms.ModelForm):
    class Meta:
        model=sendRentRequest
        fields=[
            'toolid',
            'nooftools',
            'duration'
        ]


        labels={
            'toolid':'Tool Id',
            'nooftools':'Number of tools needed',
            'duration':'Duration(in days)',
        }
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['toolid'].empty_label="Select" 
   