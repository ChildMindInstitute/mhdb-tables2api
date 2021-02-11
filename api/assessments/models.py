from django.db import models

# Create your models here.

class Questionnaire(models.Model):
    # in django an autoincrement id is already included by default

    index = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=50)


class Question(models.Model):
    
    index = models.IntegerField()
    text = models.CharField(max_length=100)
    questionaires = models.ManyToManyField(Questionnaire) #https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-many-relationships
