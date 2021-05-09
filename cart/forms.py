from django import forms


class CartAddOrgForm(forms.Form):
    sub_org_name = forms.CharField(required=False,
                                   max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    level = forms.CharField(required=False,
                            max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))


class EmailForm(forms.Form):
    email_to = forms.EmailField(required=True, max_length=255)
    accept_policy = forms.CharField(
        required=True, label="I Accept The Data Privacy Policy", widget=forms.CheckboxInput(attrs={'class': 'form-controler'}))
    
