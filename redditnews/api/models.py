from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200, unique = True)
    ups = models.IntegerField(default=0) 
    downs = models.IntegerField(default=0)
    ratio = models.FloatField(default=0)
    score = models.FloatField(default=0)
    created = models.DateField() 






    

    
    










