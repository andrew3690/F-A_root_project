from django.db import models
from datetime import date

#Dictonary that indicates days of the week
weekday ={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wendesday',4:'Thursday',5:'Friday',6:'Saturday'}

class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract =True

class Run(TimestampableMixin):
    code = models.CharField(
        max_length = 30
    )

    weekday = models.CharField(
        max_length= 20,
        #choices=weekday,
        null=True
    )

    hour = models.TimeField(
        auto_now=True
    ) 

    day = models.DateField(
        default= date.today(),
        null=True
    )

    # Might need to add recurence value, wheter is daily, weekly, monthly
    # For Future:
    #   1 - Create Runs, based on which types of runs must be made (Brazilian, USA, etc)
    #   2-  Create Runs for data fixing, only takes the format of data
    #   3-  Create Runs for researching stocks 