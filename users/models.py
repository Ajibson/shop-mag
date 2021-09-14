from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(blank=True, null=True,
                                      upload_to='profile_images')
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(blank=True, null=True, unique=False)
    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

# Password Reset code


class passwordresetcode(models.Model):
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Messages(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Admin Messages"
