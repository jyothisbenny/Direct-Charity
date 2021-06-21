from django import forms
from .models import Relationships, Categories, Hospitals, Patients
from django.forms import ModelChoiceField


class RequestForm(forms.ModelForm):
    patient_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control is-valid',
                                                                                'placeholder': 'patient name'}))

    relationship = forms.ModelChoiceField(queryset=Relationships.objects.all(), empty_label=None, required=True,
                                          widget=forms.Select(attrs={'class': 'form-control form-select',
                                                                     'placeholder': 'for'}),
                                          error_messages={'required': 'Please choose your option'})

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

    class Meta:
        model = Patients
        fields = ("patient_name", "relationship", "disease", "category", "description", "documents", "hospital",
                  "doctor_name", "required_amount")


