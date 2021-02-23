from django.db import models

# class ICD9CM(models.model):	
#     pass

# class ICD10CM(models.model):
#     pass 

# Create your models here.
class DisorderCategory(models.Model):

    name = models.CharField(max_length=200)
    # ICD9CM = models.ManyToManyField('ICD9CM')
    # ICD10CM = models.ManyToManyField('ICD10CM')

    def __str__(self):
        return self.name