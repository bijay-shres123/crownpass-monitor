from django.db import models
from django.conf import settings



# MODEL FOR REGIONS 
class Region(models.Model):
    #REGION
    #Region options
    ENGLAND = 'ENGLAND'
    SCOTLAND = 'SCOTLAND'
    WALES = 'WALES'
    NORTHERN_IRELAND = 'NORTHERN IRELAND'
    REGION_CHOICES = [
        (ENGLAND, 'ENGLAND'),
        (SCOTLAND, 'SCOTLAND'),
        (WALES, 'WALES'),
        (NORTHERN_IRELAND, 'NORTHERN_IRELAND')

    ]
    region_name= models.CharField(max_length=120, choices=REGION_CHOICES)
    
    #counties options
    Cambridgeshire = 'Cambridgeshire'
    Derbyshire = 'Derbyshire'
    Devon = 'Devon'
    East_Sussex = 'East Sussex'
    Essex = 'Essex'
    Gloucestershire = 'Gloucestershire'
    Hampshire = 'Hampshire'
    Kent = 'Kent'
    Lancashire = 'Lancashire'
    Leicestershire = 'Leicestershire'
    
    COUNTIES_CHOICES = [
        (Cambridgeshire, 'cambrigeshire'),
        (Derbyshire, 'derbyshire'),
        (Devon, 'devon'),
        (East_Sussex, 'East_sussex'),
        (Essex, 'Essex'),
        (Gloucestershire, 'gluchestershire'),
        (Hampshire,'hampshire'),
        (Kent, 'krent'),
        (Lancashire, 'lancashire'),
        (Leicestershire, 'leicestershire')

    ]
    county_name = models.CharField(max_length=120, choices=COUNTIES_CHOICES)

    city_town = models.CharField(max_length=50,)

    #CASES
    
    #STATUS OPTIONS 
    RED = 'RED'
    AMBER = 'AMBER'
    GREEN = "GREEN"
    STATUS_CHOICES = [
        (RED, 'RED'),
        (AMBER, 'AMBER'),
        (GREEN, 'GREEN')
    ]
    status = models.CharField('status',max_length=10, choices=STATUS_CHOICES)
    


#Test Result
class TestResult(models.Model):
    number_of_positive  =  models.IntegerField()
    number_of_recoverd = models.IntegerField()
    number_of_negative = models.IntegerField()

    date = models.DateField()

    county_name = models.ForeignKey(Region,null=True, on_delete=models.SET_NULL)
