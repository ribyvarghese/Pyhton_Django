from django.contrib import admin
from .models import Departments, Doctors,Booking,Contacts
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name','p_no','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking, BookingAdmin)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name','mail','subject','message')
admin.site.register(Contacts,ContactsAdmin)