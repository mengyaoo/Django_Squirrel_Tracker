from django.db import models

# Create your models here.
class Sighting(models.Model):
    Latitude=models.FloatField(max_length=100,)
    Longitude=models.FloatField(max_length=100,)
    Unique_Squirrel_ID=models.CharField(
            max_length=20,
            primary_key=True,
            unique=True,
            help_text='\n "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."',
            )

    AM="am"
    PM="pm"
    Shift_CHOICES=[(AM,"AM"),(PM,"PM"),]
    Shift=models.CharField(
            max_length=2,
            choices=Shift_CHOICES,
            default=AM,
            )

    Date=models.DateField(
            blank=True,
            )

    ADULT="adult"
    JUVENILE="juvenile"
    Age_CHOICES=[(ADULT,"Adult"),(JUVENILE,"Juvenile"),]
    Age=models.CharField(
            max_length=10,
            choices=Age_CHOICES,
            default=ADULT,
            )
