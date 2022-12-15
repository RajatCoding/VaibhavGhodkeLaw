from django.contrib import admin
from .models import ContactUs
# Register your models here.

class AdminContact_US(admin.ModelAdmin):
      list_display = ["first_name", "last_name", "email", "mobile_no","message",]

admin.site.register(ContactUs , AdminContact_US)

