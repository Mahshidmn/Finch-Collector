from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Toy(models.Model):
    name= models.CharField(max_length=256)
    color = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
    
    def __str__(self):
        return self.name
    

class Finch(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('')
    meal = models.CharField (
    max_length = 1,
    choices = MEALS,
    default = MEALS[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete = models.CASCADE)
    def __str__(self):
        return f"{ self.get_meal_display() } on { self.date }"
    class Meta: 
        ordering = ['-date']

