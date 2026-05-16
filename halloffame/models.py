from django.db import models

class Legend(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    era = models.CharField(max_length=50)
    championships = models.IntegerField()
    wins = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to='halloffame/', blank=True, null=True)

    def __str__(self):
        return self.name