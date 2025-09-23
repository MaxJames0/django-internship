from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone_number', 'username','email', 'password1', 'password2']
        
        
        def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            if len(phone_number) != 11:
                raise forms.ValidationError("شماره تلفن باید 11 رقم باشد.")
            return phone_number
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "phonenumber",
            "autofocus": True
        })
    )
    password = forms.CharField(
        label = "password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "password"
        }), 
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username.isdigit():
            raise forms.ValidationError("لطفا فقط عدد وارد کنید")
        if len(username) != 11:
            raise forms.ValidationError("شماره باید 11 رقم باشد")
        return username

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'profile_pic']