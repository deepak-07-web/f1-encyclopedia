from django.db import models

class Season(models.Model):
    year = models.IntegerField(unique=True)
    drivers_champion = models.CharField(max_length=100)
    constructors_champion = models.CharField(max_length=100)
    total_races = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    
    # Images
    season_image = models.ImageField(upload_to='seasons/', blank=True, null=True)
    driver_champion_image = models.ImageField(upload_to='seasons/drivers/', blank=True, null=True)
    constructor_champion_image = models.ImageField(upload_to='seasons/constructors/', blank=True, null=True)


    def __str__(self):
        return str(self.year)

class SeasonResult(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    position = models.IntegerField()
    driver = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.DecimalField(max_digits=6, decimal_places=1)

    def __str__(self):
        return f"{self.season.year} - P{self.position} - {self.driver}"