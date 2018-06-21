from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    try:
        if 'http' in value:
            new_value = value
            URLValidator(new_value)
            print(new_value)
        else:
            new_value = f'http://{value}'
            print(new_value)
            URLValidator(new_value)
    except:
        raise ValidationError("input a valid URL")
    return new_value