from django import forms

from .models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
    

    labels = {
        'name':"Name: ",
        'mail':"Email: ",
        'subject':"Suject: ",
        'message':"Please write Message: ",       

    }