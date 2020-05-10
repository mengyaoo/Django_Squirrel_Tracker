from django.db import models


class squirrel_site(models.Model):
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
            auto_now=False,
            )

    ADULT="adult"
    JUVENILE="juvenile"
    Age_CHOICES=[(ADULT,"Adult"),(JUVENILE,"Juvenile"),]
    Age=models.CharField(
            max_length=10,
            choices=Age_CHOICES,
            default=ADULT,
            )

    GRAY = "Gray"
    CINNAMON = "Cinnamon"
    BLACK = "Black"
    WHITE = "White"
    Fur_CHOICES = [(GRAY,"Gray"),(CINNAMON,"Cinnamon"),(BLACK,"Black"),(WHITE,"White"),]
    Primary_fur_color=models.CharField(
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


        Specific_location=models.TextField(
        max_length=500,
        blank=True,
        )

    Running=models.BooleanField(
        default=False,
        )

    Chasing=models.BooleanField(
        default=False,
        )

    Climbing=models.BooleanField(
        default=False,
        )

    Eating=models.BooleanField(
        default=False,
        )

    Foraging=models.BooleanField(
        default=False,
        )

    Other_activities=models.TextField(
        max_length=500,
        blank=True,
        )

   Kuks=models.BooleanField(
       default=False,
       help_text='\n A squirrel was found qukking.',
       )


   Quaas=models.BooleanField(
       default=False,
       help_text='\n A squirrel was found quaaing.',
       )


   Moans=models.BooleanField(
       default=False,
       help_text='\n A squirrel was found moaning.',
       )


   Tail_flags=models.BooleanField(
       default=False,
       help_text="\n A squirrel was seen flagging its tail.",
       )


   Tail_twitches=models.BooleanField(
       default=False,
       help_text='\n A squirrel was seen twitching its tail.',
       )

   Approaches=models.BooleanField(
       default=False,
       help_text='\n A squirrel was seen approaching human, seeking food.',
       )


   Indifferent=models.BooleanField(
       default=False,
       help_text='\n A squirrel was indifferent to human beings’ presence.',
       )

   Runs_from=models.BooleanField(
       default=False,
       help_text='\n A squirrel was seen running away.',
       )

   Other_interactions=models.TextField(
       max_length=500,
       blank=True,
       help_text='\n Other types of interactions between squirrels and humans were noticed.',
       )

