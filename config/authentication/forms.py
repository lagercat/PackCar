from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(attrs={
                                   'required': 'required',
                                   'placeholder': "Username"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'required': 'required',
               'placeholder': "Password"}),
                               label='Password')


class UserRegisterForm(forms.ModelForm):
    retypepassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype password',
        'label': 'Retype password',
        'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput({'required': 'required',
                                         'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'required': 'required',
                                                   'placeholder': 'Password'})
        }

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count():
            raise forms.ValidationError("This username already exists")
        elif (
                not (user_name.isalnum() or user_name.isalpha())
        ):
            raise forms.ValidationError("Username contains invalid characters")
        return user_name

    def clean_retypepassword(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['retypepassword']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password2
