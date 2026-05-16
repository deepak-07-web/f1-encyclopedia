from django.db import models

class Tyre(models.Model):
    COMPOUND_CHOICES = [
        ('soft', 'Soft'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('intermediate', 'Intermediate'),
        ('wet', 'Wet'),
    ]

    name = models.CharField(max_length=50)
    compound = models.CharField(max_length=20, choices=COMPOUND_CHOICES)
    colour = models.CharField(max_length=7, default='#ffffff')
    description = models.TextField()
    best_used_for = models.CharField(max_length=200)
    average_stint_length = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tyres/', blank=True, null=True)

    def __str__(self):
        return self.name
