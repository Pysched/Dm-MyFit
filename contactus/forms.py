from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):

    ContactUs = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = ContactUs
        fields = ('full_name', 'email', 'phone_number', 'message')
