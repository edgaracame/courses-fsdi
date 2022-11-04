from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    required_css_class='required-field'
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'aria-label': 'Email', 'aria-describedby':'addon-wrapping'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'aria-describedby':'addon-wrapping'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'type':'password', 'aria-describedby':'addon-wrapping'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password', 'type':'password', 'aria-describedby':'addon-wrapping'})

class PasswordChangedForm(PasswordChangeForm):
    required_css_class='required-field'
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Current Password', 'type':'password', 'aria-label': 'Email', 'aria-describedby':'addon-wrapping'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password', 'type':'password', 'aria-label': 'Email', 'aria-describedby':'addon-wrapping'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password', 'type':'password', 'aria-label': 'Email', 'aria-describedby':'addon-wrapping'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')