from tabnanny import verbose
from django.urls import reverse
from django.db import models

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    class Meta:
        verbose_name = 'finch'
        verbose_name_plural = 'finches'

    def __str__(self):
        return f'{self.name}, ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})



# finches = [
#   Finch('Ryland', 'saffron', 'chill, muchos siestas', 3),
#   Finch('Mehj', 'blue', 'pretty bird, sips tea', 2),
#   Finch('Dave', 'spice', 'spicy-boy, charming cat-collector, flex-box girrrrl', 4),
#   Finch('Devlin', 'society', 'HIGH-society', 4),
# ]