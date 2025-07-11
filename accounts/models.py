from django.db import models
from django.contrib.auth.models import User

class UserInterest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    interests = models.ManyToManyField(UserInterest, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    full_name_displayed = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
