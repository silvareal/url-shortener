from django.db import models
from .utils import code_generator, create_shorcode
from django.conf import settings

from .validation import validate_url


SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self, items=None):
        print(items)
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_code = 0
        for q in qs:
            q.shortcode = create_shorcode(q)
            print(q.id)
            q.save()
            new_code += 1
        return f'new code made {new_code}'


class KirrURL(models.Model):
    url = models.CharField(max_length=300, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shorcode(self)
        super(KirrURL, self).save(*args, **kwargs)