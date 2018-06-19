import string
import random
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shorcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    print(instance)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return code_generator(size=size)
    return new_code