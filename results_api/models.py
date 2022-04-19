from django.db import models
from regions_api.models import Region 
#Test Result
class Results(models.Model):
    number_of_positive  =  models.IntegerField()
    number_of_recoverd = models.IntegerField()
    number_of_negative = models.IntegerField()

    date = models.DateField()

    county_name = models.ForeignKey(Region,null=True, on_delete=models.SET_NULL)