from django.db import models
from shorten.models import KirrURL

# Create your models here.

class ClickEventManager(models.Manager):
    def createcount(self, kirrinstance):
        if isinstance(kirrinstance, KirrURL):
            obj, created = self.get_or_create(kirr_url=kirrinstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    kirr_url = models.ForeignKey(KirrURL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        count_str = str(self.count)
        kirr_url = self.kirr_url.url
        return f'URL=>{kirr_url}  CLICKNO=>{count_str}'
