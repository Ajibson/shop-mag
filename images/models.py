from django.db import models
from users.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Image(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    image_name = models.CharField(max_length=250)
    image_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=0)
    amount_made = models.IntegerField(default=0)
    number_of_download = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.image_name
