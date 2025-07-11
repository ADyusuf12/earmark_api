from django.db import models
from accounts.models import UserProfile

class PropertyCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    LISTING_TYPE_CHOICES = [
        ('SALE', 'For Sale'),
        ('RENT', 'For Rent'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    category = models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True, blank=True)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE_CHOICES, default='SALE')
    owner_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
