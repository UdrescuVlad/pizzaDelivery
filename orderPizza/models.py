from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Pizza(models.Model):
    PIZZA_TYPE = (
        ('Happy', 'Happy Pizza'),
        ('Joshua', 'Joshua Pizza'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    bonus = models.CharField(max_length=50)
    pizza_type = models.CharField(max_length=6, choices=PIZZA_TYPE, default='Happy')

    def __str__(self) -> str:
        return self.name+'$'+self.price

class DailyMenu(models.Model):
    class DayOfWeek(models.TextChoices):
        MO = "MONDAY"
        TU = "TUESDAY"
        WE = "WEDNESDAY"
        TH = "THURSDAY"
        FR = "FRIDAY"
        SAT = "SATURDAY"
        SU = "SUNDAY"
    
    first_course = models.TextField(max_length=200)
    second_course = models.TextField(max_length=200)
    drink = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.CharField(max_length=9, choices=DayOfWeek.choices, default=DayOfWeek.MO)

    def __str__(self) -> str:
        return self.day+'_'+self.first_course+'_'+self.second_course
