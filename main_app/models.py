from email.policy import default
from tabnanny import verbose
from django.urls import reverse
from django.db import models

# Create your models here.

VIEWS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class House(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('house_detail', kwargs={'house_id': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    houses = models.ManyToManyField(House)

    class Meta:
        verbose_name = 'finch'
        verbose_name_plural = 'finches'

    def __str__(self):
        return f'{self.name}, ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    

class Watching(models.Model):
    date = models.DateField('Viewing Date')
    view = models.CharField(
        max_length=1,
        choices=VIEWS,
        default=VIEWS[0][0]
        )
    
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_view_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"photo for finch_id: {self.finch_id} @{self.url}"


# finches = [
#   Finch('Ryland', 'saffron', 'chill, muchos siestas', 3),
#   Finch('Mehj', 'blue', 'pretty bird, sips tea', 2),
#   Finch('Dave', 'spice', 'spicy-boy, charming cat-collector, flex-box girrrrl', 4),
#   Finch('Devlin', 'society', 'HIGH-society', 4),
# ]