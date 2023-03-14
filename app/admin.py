from django.contrib import admin
from app.models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','username','email','phone','subject','message','created_at')
