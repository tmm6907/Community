from django.db import models
from phone_field import PhoneField

# Create your models here.


class Place(models.Model):
    categories = (
        ('grocery store', 'grocery store'),
        ('primary care', 'primary care'),
        ('bank', 'bank'),
        ('park', 'park'),
        ('mental health service', 'mental health'),
        ('emergency service', 'emergency service'),
        ('pharmacy', 'pharmacy'),
        ('dental care', 'dental care'),
        ('post office', 'post office'),
        ('trail', 'trail'),
        ('public transportation', 'public transportation'),
        ('fedex', 'fedex'),
        ('ups', 'ups'),
    )
    name = models.CharField(max_length=48)
    formatted_address = models.CharField(max_length=96, unique=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number', null=True)
    zip_code = models.CharField(max_length=5)
    url = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    photos = models.URLField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=24, choices=categories)

    def __string__(self):
        return self.name

    def to_hex(self):
       return hex(self.pk)
