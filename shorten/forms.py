from django import forms
from .validation import validate_url

class SubmitURLForm(forms.Form):
    url = forms.CharField(label="Submit URL",
                validators=[validate_url],
                widget = forms.TextInput(
                    attrs ={
                        "placeholder": "paste url for shortening ",
                        "class": "form-control",
                        "autocomplete": "off"
                        }

                )
    )