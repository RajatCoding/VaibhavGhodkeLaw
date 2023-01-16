from django.contrib import admin
from .models import ContactUs,Carriers
# Register your models here.

class AdminContact_US(admin.ModelAdmin):
      list_display = ["first_name", "last_name", "email", "mobile_no",]
class AdminCarriers(admin.ModelAdmin):
      list_display = ["first_name", "last_name", "email", "mobile_no",'resume']
admin.site.register(ContactUs , AdminContact_US)
admin.site.register(Carriers , AdminContact_US)


