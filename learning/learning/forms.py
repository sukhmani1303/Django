from django import forms

class testForm(forms.Form):
    email = forms.CharField(label = "Enter email", widget=forms.EmailInput)
    passw = forms.CharField(label = "Enter password", widget=forms.PasswordInput)