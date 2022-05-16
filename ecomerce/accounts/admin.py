from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ( 'id','email' , 'first_name' , 'last_name' , 'username' , 'last_login','date_joined','is_active')

    filter_horizontal = ()
    list_filter = ('date_joined','email')
    fieldsets = ()
    
# Register your models here.
admin.site.register(Account, AccountAdmin)
