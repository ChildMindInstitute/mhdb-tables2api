from django.db import models

from django.contrib.auth.models import User



### models to be defined in another module
class Respondent(models.Model):
    pass

class Subject(models.Model):
    pass

class Age(models.Model):
    pass

class Disorder(models.Model):
    pass


# move to resources module
class Language(models.Model):

    index = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    index_language = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    snomedct_id = models.PositiveIntegerField()




class Author(models.Model):
    models.CharField(max_length=200)


class Reference(models.Model):

    index = models.IntegerField()
    title = models.CharField(max_length=300)
    link = models.URLField()     
    authors = models.ManyToManyField(Author)
    entry_date = models.DateField()
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    pubdate = models.DateField(null=True)
    PubMedID = models.PositiveIntegerField(null=True)
    cogatlas_node_id = models.PositiveIntegerField(null=True)   
    cogatlas_prop_id = models.PositiveIntegerField(null=True)


class Questionnaire(models.Model):
    
    index = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.URLField(null=True)
    description = models.CharField(max_length=1500)
    abbreviation = models.CharField(max_length=50)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)
    year = models.PositiveIntegerField()
    use_with_assessments = models.ManyToManyField('self')
    indices_reference = models.ForeignKey(Reference, null=True, on_delete=models.SET_NULL)
    # ANIRUDH: LEFT column
    index_license = models.PositiveIntegerField(null=True) #change to foreign keys at a later date
    index_language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    # indices_language_not_in_mhdb = models.ManyToManyField(Language) # what is this column for?
    # LEFT column errors                
    indices_respondent = models.ManyToManyField('Respondent')    # need to find this table in the spreadsheets
    indices_subject = models.ManyToManyField('Subject')       # need to find this table in the spreadsheets
    age_min = models.PositiveSmallIntegerField(null=True)
    age_max = models.PositiveSmallIntegerField(null=True)
    number_of_questions = models.PositiveSmallIntegerField(null=True)
    number_of_questions_with_ranges = models.PositiveIntegerField(null=True)
    minutes_to_complete = models.PositiveIntegerField(null=True)
    minutes_to_complete_with_ranges = models.CharField(null=True, max_length=10)
    indices_age = models.ManyToManyField('Age') # need to find this table in the spreadsheets
    indices_disorder = models.ManyToManyField('Disorder')
    # indices_disorder_category         # this field in the the disorder table
    # ANIRUDH: LEFT column.1
    # ANIRUDH: RIGHT column
    # indices_disorder_subcategory      # this field in the the disorder table
    # indices_disorder_subsubcategory   # this field in the the disorder table


class Question(models.Model):
    
    index = models.IntegerField()
    text = models.CharField(max_length=200)
    questionaires = models.ManyToManyField(Questionnaire) #https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-many-relationships


