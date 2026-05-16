from django.db import models

class Driver(models.Model):
    # Basic Info
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    driver_number = models.IntegerField(null=True, blank=True)
    abbreviation = models.CharField(max_length=3)
    
    # Career Stats
    races = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    podiums = models.IntegerField(default=0)
    pole_positions = models.IntegerField(default=0)
    fastest_laps = models.IntegerField(default=0)
    championships = models.IntegerField(default=0)
    
    # Extra Info
    bio = models.TextField()
    debut_year = models.IntegerField()
    
    # Image
    image = models.ImageField(upload_to='drivers/', blank=True, null=True)
    helmet_image = models.ImageField(upload_to='helmets/', blank=True, null=True)
    action_image = models.ImageField(upload_to='drivers/action/', blank=True, null=True)
    podium_image = models.ImageField(upload_to='drivers/podium/', blank=True, null=True)
    young_career_image = models.ImageField(upload_to='drivers/young/', blank=True, null=True)
    car_image = models.ImageField(upload_to='drivers/car/', blank=True, null=True)



    def __str__(self):
        return self.name