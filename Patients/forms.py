from django import forms
from .models import Relationships, Categories, Hospitals, Patients
from django.forms import ModelChoiceField

from django.core.exceptions import ValidationError


class RequestForm(forms.ModelForm):
    patient_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'patient name'}))

    relationship = forms.ModelChoiceField(queryset=Relationships.objects.all(), empty_label=None, required=True,
                                          widget=forms.Select(attrs={'class': 'form-control form-select',
                                                                     'placeholder': 'for'}),
                                          error_messages={'required': 'Please choose your option'})

    patient_photo = forms.FileField(help_text='max. 42 megabytes')

    disease = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Disease Name'}))

    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label=None, required=True,
                                      widget=forms.Select(attrs={'class': 'form-control form-select'}),
                                      error_messages={'required': 'Please choose your option'})

    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                              'placeholder': 'please enter some details about patient and hospital',
                                                                              'maxlength': '200'}),
                                  error_messages={'required': 'Please enter some details about the patient'})

    documents = forms.FileField(help_text='max. 42 megabytes')

    hospital = forms.ModelChoiceField(queryset=Hospitals.objects.all(), empty_label=None, required=True,
                                      widget=forms.Select(attrs={'class': 'form-control form-select'}),
                                      error_messages={'required': 'Please choose your option'})

    doctor_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                               'placeholder': 'Doctor name'}))

    required_amount = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                      'placeholder': 'Enter required amount'}))

    upi_id = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control is-valid',
                                                                              'placeholder': 'UPI ID'}))

    upi_id2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control is-valid',
                                                                               'placeholder': 'confirm UPI ID'}))

    class Meta:
        model = Patients
        fields = (
            "patient_name", "relationship", "patient_photo", "disease", "category", "description", "documents",
            "hospital", "doctor_name", "required_amount", "upi_id")

    def clean(self):
        cleaned_data = super(RequestForm, self).clean()
        upi_id = cleaned_data.get("upi_id")
        upi_id2 = cleaned_data.get("upi_id2")

        if upi_id != upi_id2:
            self._errors['upi_id2'] = self.error_class(['upi ids not matching.'])
            del self.cleaned_data['upi_id2']
        return cleaned_data
