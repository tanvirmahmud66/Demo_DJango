import email
from django import forms
from django.core import validators

class ContactInput(forms.Form):
    name = forms.CharField(label='Enter your Name')
    email = forms.EmailField(label_suffix="-", initial='email@email.com')
    phone = forms.CharField(initial='+880')
    address = forms.CharField(disabled=True, initial='disabled')
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    massage = forms.CharField(widget=forms.Textarea, disabled=True, initial='disabled')
    file = forms.CharField(widget=forms.FileInput, disabled=True)
    checkbox = forms.CharField(widget=forms.CheckboxInput, disabled=True)

    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['password']
        if rightpass != wrongpass:
            raise forms.ValidationError("Password doesn't match")
