from django.db import models
from users.models import User
from django.utils import timezone
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Image(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="images", null=True, blank=True)
    image_name = models.CharField(max_length=250)
    image = ResizedImageField(
        size=[350, 350], upload_to="images", blank=True, null=True, force_format='PNG')
    image_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=0)
    amount_made = models.IntegerField(default=0, blank=True)
    number_of_download = models.IntegerField(default=0, blank=True)
    # description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.image_name
