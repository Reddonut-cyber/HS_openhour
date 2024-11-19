# myapp/forms.py
from django import forms

class StringForm(forms.Form):
    input_string = forms.CharField(label="Enter a string", max_length=100)
