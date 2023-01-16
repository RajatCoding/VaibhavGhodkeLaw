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
        'first_name': forms.TextInput(attrs = {'class':'form-control shadow-lg','placeholder':'Enter First Name'}),

        'last_name': forms.TextInput(attrs = {'class':'form-control shadow-lg','placeholder':'Enter Last Name'}),

        'mobile_no': forms.TextInput(attrs = {'class':'form-control shadow-lg','placeholder':'Mobile Number'}),

        'email': forms.EmailInput(attrs = {'class':'form-control shadow-lg','placeholder':'Enter your email','required':'true'}),

        'message': forms.Textarea(attrs = {'class':'form-control shadow-lg','placeholder':'Enter your message','rows':4}),
        }

class Carrier_form(forms.ModelForm): 
 
   class Meta:
        model = Carriers
        fields = ["first_name", "last_name", "email", "mobile_no","resume", ]
        labels = {"email": "Email", 'resume': "Resume"}

        error_messages = {

         'first_name': {'required': 'Naam Likhna Jaruri Hai'}, 'mobile_no' :{
                     "required": 'Mobile numbser is required',
                     "unique":"You have already submitted the form",
                     },

         }
 

        widgets = {
        'first_name': forms.TextInput(attrs = {'class':'form-control shadow-lg','placeholder':'Enter First Name'}),

        'last_name': forms.TextInput(attrs = {'class':'form-control shadow-lg','placeholder':'Enter Last Name'}),

        'mobile_no': forms.TextInput(attrs = {'class':'form-control shadow-lg','placeholder':'Mobile Number'}),

        'email': forms.EmailInput(attrs = {'class':'form-control shadow-lg','placeholder':'Enter your email','required':'true'}),

        'resume': forms.FileInput(attrs = {'class':'form-control shadow-lg','placeholder':'Upload your resume','required':'true'}),

        
        }

