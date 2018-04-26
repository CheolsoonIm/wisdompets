from django.db import models

class Pet(models.Model):

    SEX_CHOICES = [('M', 'Male',), ('F', 'Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True) # breed may not be known
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True) # choices attribute uses constant (pets may be unable to be sexed)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) # in case pets are rescued with unknown age (blank int = 0, so use null=True instead)
    vaccinations = models.ManyToManyField('Vaccine', blank=True) # many to many model to Vaccine

class Vaccine(models.Model):
    name = models.CharField(max_length=50)    

    # override str method - tells django what the string respresentation of this model should be
    def __str__(self):
        return self.name
