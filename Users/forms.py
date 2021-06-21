from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

from django.utils.translation import ugettext_lazy as _


# Create your forms here.

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                               'placeholder': 'first name'}),
                                 error_messages={'required': 'Please enter your first name'})

    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                              'placeholder': 'last name'}),
                                error_messages={'required': 'Please enter your first name'})

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'id': 'inputEmail4', 'placeholder': 'Email'}),
                             error_messages={'unique': "This email has already been registered."})

    username = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'username'}),
                               error_messages={'required': 'username already taken'})

    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'please enter your 10 digit phone number',  'maxlength': '10'}),
                            error_messages={'required': 'Please enter your 10 digit phone number',
                                            'unique': 'phone no already registered, try login'})

    password1 = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail4',
                                                              'placeholder': 'Enter password'}),
                                error_messages={
                                    'required': 'Please enter a password with Capital letters, small letters and numbers'})

    password2 = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail4',
                                                              'placeholder': 'Retype the same password'}),
                                error_messages={
                                    'required': 'Please enter a password with Capital letters, small letters and numbers'})

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data['email']
    #     if MyUser.objects.filter(email="email").exists():
    #         raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
    #     return email

    class Meta:
        model = MyUser
        fields = ("first_name", "last_name", "username", "email", "phone", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
