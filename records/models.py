from django.db import models

class Record(models.Model):
    CATEGORY_CHOICES = [
        ('driver', 'Driver Record'),
        ('constructor', 'Constructor Record'),
        ('race', 'Race Record'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100)
    holder = models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='records/', blank=True, null=True)

    def __str__(self):
        return self.title