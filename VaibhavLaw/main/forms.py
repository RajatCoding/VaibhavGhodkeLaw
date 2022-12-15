from django import forms
from . models import *

class Contact_US_form(forms.ModelForm):  
   class Meta:
        model = ContactUs
        fields = ["first_name", "last_name", "email", "mobile_no","message", ]
        labels = {"email": "Email"}
        error_messages = {'first_name': {'required': 'Naam Likhna Jaruri Hai'},  
					 }

        widgets = {
        'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}),

        'last_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Last Name'}),

        'mobile_no': forms.TextInput(attrs = {'class':'form-control','placeholder':'Mobile Number'}),

        'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter your email','required':'true'}),

        'message': forms.Textarea(attrs = {'class':'form-control','placeholder':'Enter your message','rows':4}),

  

        }
