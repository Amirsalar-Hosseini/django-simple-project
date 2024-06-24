from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()