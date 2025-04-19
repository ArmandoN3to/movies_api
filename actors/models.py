from django.db import models

# Create your models here.

NATIONALITIES_CHOICES = (
    ('USA','Estados Unidos'),
    ('BRAZIL','Brasil'),
    ('CANADA','Canada'),
    ('ARGENTINA','Argentina'),
    ('MEXICO','Mexico'),
    ('UK','Reino Unido'),
    ('GERMANY','Alemania'),
    ('FRANCE','Francia'),
    ('SPAIN','Espanha'),
    ('ITALY','Italia')
    )

class Actor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField(null=True,blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITIES_CHOICES,
        blank=True,
        null=True,)

    def __str__(self):
        return self.name
