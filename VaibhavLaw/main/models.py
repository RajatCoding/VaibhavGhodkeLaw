from django.db import models
import re
from django.core.exceptions import ValidationError
# Create your models here.
def mobile_validate(value):
    val = re.fullmatch("[6-9]\d{9}",value)
    if val == None:
        raise ValidationError("Enter valid mobile number. should startwith(6,7,8,9) and contain 10digits")

class ContactUs(models.Model):
      first_name = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)
      email = models.EmailField(max_length=100)
      mobile_no = models.CharField(max_length=10, validators=[mobile_validate])
      message = models.TextField()
    
class Client_testonomial(models.Model):
    client_name = models.CharField(max_length=30)
    client_message = models.CharField(max_length=500)
    client_image = models.ImageField(upload_to="client_image")
