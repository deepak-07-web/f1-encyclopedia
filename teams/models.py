from django.db import models

class Team(models.Model):
    # Basic Info
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    base = models.CharField(max_length=100)
    founded = models.IntegerField()
    team_principal = models.CharField(max_length=100)
    engine_supplier = models.CharField(max_length=50)
    championships = models.IntegerField(default=0)
    
    # Colors
    team_color = models.CharField(max_length=7, default='#e10600')
    
    # Extra Info
    bio = models.TextField()
    
    # Images
    logo = models.ImageField(upload_to='teams/logos/', blank=True, null=True)
    car_image = models.ImageField(upload_to='teams/cars/', blank=True, null=True)
    garage_image = models.ImageField(upload_to='teams/garage/', blank=True, null=True)
    podium_image = models.ImageField(upload_to='teams/podium/', blank=True, null=True)

    def __str__(self):
        return self.name