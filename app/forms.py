from django import forms
from .models import *
# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     email=forms.EmailField()
#     message=forms.CharField(widget=forms.Textarea)

class modelContactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'