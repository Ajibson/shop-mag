from django.db import models
from images.models import Image
from django.utils import timezone


class Payment(models.Model):
    image_for = models.ForeignKey(
        Image, on_delete=models.SET_NULL, blank=True, null=True)
    reference_id = models.UUIDField()
    amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return str(self.reference_id)
