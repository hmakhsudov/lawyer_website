# forms.py

from django import forms

class EnrollmentForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
