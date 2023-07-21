from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'p_name':"Patients Name: ",
            'p_no':"Patient Number: ",
            'p_email':"Patient Email: ",
            'doc_name':"Department Name: ",
            'booking_date':"Booking Date: ",
        }