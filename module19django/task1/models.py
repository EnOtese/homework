from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.TextField()
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title