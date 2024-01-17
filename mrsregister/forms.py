from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)