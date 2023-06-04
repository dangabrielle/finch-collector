from django.db import models
from django.urls import reverse

# Create your models here.


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f'A {self.color} {self.name}'

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # redirects back to the detail page after creating a cat
        return reverse('detail', kwargs={'finch_id': self.id})


class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # Create a cat_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
