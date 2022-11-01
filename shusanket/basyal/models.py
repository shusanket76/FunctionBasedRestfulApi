from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollnumber = models.IntegerField()
    address = models.CharField(max_length=100)
    
    