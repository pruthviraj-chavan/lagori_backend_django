from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='activities/')  # Store images in 'media/activities/'

    def __str__(self):
        return self.title