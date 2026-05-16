from django.db import models

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.term

    class Meta:
        ordering = ['term']
