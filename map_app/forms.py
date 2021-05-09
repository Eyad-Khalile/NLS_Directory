from django import forms
from .models import Countries, Orgs

# ORG FORM - CREATE / UPDATE
class NewOrgForm(forms.ModelForm):
    class Meta:
        model = Orgs
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


# COUNTRY FORM - CREATE / UPDATE
class CountryForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = '__all__'

# CONTACT FORM
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=100)
    contact_email = forms.EmailField(required=True, max_length=100)
    contact_subject = forms.CharField(required=True, max_length=255)
    contact_message = forms.CharField(
        required=True, max_length=5000, widget=forms.Textarea)

# ACCEPT COOKIE FORM
class AcceptCookieForm(forms.Form):
    accept = forms.CharField(
        required=True, widget=forms.CheckboxInput(attrs={"checked": True, 'class': 'd-none'}))
    current_path = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"class": 'd-none'}))
