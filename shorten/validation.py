from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    reg_url = value
    if 'http' in reg_url:
        new_value = reg_url
    else:
        new_value = 'http://' + value
        print(new_value)
    try:
        url_validator(new_value)
    except:
        raise ValidationError("input a valid URL")
    return new_value