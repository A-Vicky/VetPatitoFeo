from django.db import models
import datetime

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    first_lname = models.CharField(max_length=100)
    second_lname = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + ' ' + self.first_lname
    
class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    first_lname = models.CharField(max_length=100)
    second_lname = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.first_name + ' ' + self.first_lname
    
class Pet(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    behavior = models.TextField()
    age = models.IntegerField()
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Appointment(models.Model):
    pet = models.ForeignKey(
        Pet, on_delete=models.SET_DEFAULT, default=-1
    )
    profesional = models.ForeignKey(
        Employee, on_delete=models.SET_DEFAULT, default=-1
    )
    description = models.TextField()
    comments = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.id