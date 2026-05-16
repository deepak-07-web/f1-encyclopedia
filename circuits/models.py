from django.db import models

class Circuit(models.Model):
    # Basic Info
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    length_km = models.DecimalField(max_digits=5, decimal_places=3)
    turns = models.IntegerField()
    drs_zones = models.IntegerField()
    first_gp_year = models.IntegerField()
    lap_record_time = models.CharField(max_length=20, blank=True, null=True)
    lap_record_holder = models.CharField(max_length=100, blank=True, null=True)
    lap_record_year = models.IntegerField(blank=True, null=True)

    # Extra Info
    bio = models.TextField()

    # Images
    track_image = models.ImageField(upload_to='circuits/tracks/', blank=True, null=True)
    aerial_image = models.ImageField(upload_to='circuits/aerial/', blank=True, null=True)
    corner_image = models.ImageField(upload_to='circuits/corners/', blank=True, null=True)

    def __str__(self):
        return self.name