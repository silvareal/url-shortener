from django import forms
from .validation import validate_url, validate_dot_com

class SubmitURLForm(forms.Form):
    url = forms.CharField(label="",
                validators=[validate_url, validate_dot_com],
                widget = forms.TextInput(

                    attrs ={
                        "placeholder": "paste url for shortening ",
                        "class": "form-control",
                        "autocomplete": "off",
                        "value": "",
                        }

                )
    )