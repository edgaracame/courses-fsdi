from django.contrib.auth.forms import UserCreationForm
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