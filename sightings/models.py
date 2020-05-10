from django.db import models


class Sighting(models.Model):
    latitude=models.FloatField(max_length=100,)
    longitude=models.FloatField(max_length=100,)
    unique_squirrel_id=models.CharField(
            max_length=20,
            primary_key=True,
            unique=True,
            help_text='\n "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."',
            )

    AM="am"
    PM="pm"
    Shift_CHOICES=[(AM,"AM"),(PM,"PM"),]
    shift=models.CharField(
            max_length=2,
            choices=Shift_CHOICES,
            default=AM,
            )

    date=models.DateField(
            auto_now=False,
            )

    ADULT="adult"
    JUVENILE="juvenile"
    Age_CHOICES=[(ADULT,"Adult"),(JUVENILE,"Juvenile"),]
    age=models.CharField(
            max_length=10,
            choices=Age_CHOICES,
            default=ADULT,
            )

    GRAY = "Gray"
    CINNAMON = "Cinnamon"
    BLACK = "Black"
    WHITE = "White"
    Fur_CHOICES = [(GRAY,"Gray"),(CINNAMON,"Cinnamon"),(BLACK,"Black"),(WHITE,"White"),]
    primary_fur_color=models.CharField(
        max_length=10,
        choices=Fur_CHOICES,
        default=GRAY,
        )

    Ground_Plane="GP"
    Above_Ground="AG"
    Location_CHOICES=[(Ground_Plane,"Ground Plane"),(Above_Ground,"Above Ground"),]
    Location=models.CharField(
        max_length=20,
        choices=Location_CHOICES,
        default=Ground_Plane,
        help_text ='the location of where the squirrel was when first sighted.',
        )


    specific_location=models.TextField(
        max_length=500,
        blank=True,
        )

    running=models.BooleanField(
        default=False,
        )

    chasing=models.BooleanField(
        default=False,
        )

    climbing=models.BooleanField(
        default=False,
        )

    eating=models.BooleanField(
        default=False,
        )

    foraging=models.BooleanField(
        default=False,
        )

    other_activities=models.TextField(
        max_length=500,
        blank=True,
        )

    kuks=models.BooleanField(
        default=False,
        help_text='\n A squirrel was found qukking.',
        )


    quaas=models.BooleanField(
        default=False,
        help_text='\n A squirrel was found quaaing.',
        )


    moans=models.BooleanField(
        default=False,
        help_text='\n A squirrel was found moaning.',
        )


    tail_flags=models.BooleanField(
        default=False,
        help_text="\n A squirrel was seen flagging its tail.",
        )


    tail_twitches=models.BooleanField(
        default=False,
        help_text='\n A squirrel was seen twitching its tail.',
        )
 
    approaches=models.BooleanField(
        default=False,
        help_text='\n A squirrel was seen approaching human, seeking food.',
        )


    indifferent=models.BooleanField(
        default=False,
        help_text='\n A squirrel was indifferent to human beings’ presence.',
        )

    runs_from=models.BooleanField(
        default=False,
        help_text='\n A squirrel was seen running away.',
        )

    Other_interactions=models.TextField(
        max_length=500,
        blank=True,
        help_text='\n Other types of interactions between squirrels and humans were noticed.',
        )

