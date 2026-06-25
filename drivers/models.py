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
    team_name = models.CharField(max_length=100, blank=True, null=True)
    team_color = models.CharField(max_length=7, default='#e10600', help_text='Use a hex color for the driver/team accent line.')
    
    # Image
    image = models.ImageField(upload_to='drivers/', blank=True, null=True)
    helmet_image = models.ImageField(upload_to='helmets/', blank=True, null=True)
    action_image = models.ImageField(upload_to='drivers/action/', blank=True, null=True)
    podium_image = models.ImageField(upload_to='drivers/podium/', blank=True, null=True)
    young_career_image = models.ImageField(upload_to='drivers/young/', blank=True, null=True)
    car_image = models.ImageField(upload_to='drivers/car/', blank=True, null=True)



    def __str__(self):
        return self.name


class DriverTeamPeriod(models.Model):
    driver = models.ForeignKey(Driver, related_name='team_periods', on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    team_color = models.CharField(max_length=7, default='#e10600', help_text='Use a hex color for the team period accent.')
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True, help_text='Leave empty if the driver is currently with this team.')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['start_year', 'order']

    def __str__(self):
        end_label = self.end_year if self.end_year else 'Present'
        return f"{self.driver.name} — {self.team_name} ({self.start_year}-{end_label})"

    def active_end_year(self):
        from datetime import date
        return self.end_year or date.today().year

    def range_label(self):
        return f"{self.start_year}-{self.end_year if self.end_year else 'Present'}"

    def duration_years(self):
        return self.active_end_year() - self.start_year + 1
