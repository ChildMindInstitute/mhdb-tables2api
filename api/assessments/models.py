from django.db import models

from django.contrib.auth.models import User
from resources.models import Language
from disorders.models import DisorderCategory

### models to be defined in another module
class Respondent(models.Model):
    pass

class Subject(models.Model):
    pass

class Age(models.Model):
    pass

class Author(models.Model):
    
    surname = models.CharField(max_length=200,)
    first_initial = models.CharField(max_length=1, null=True)
    middle_initial = models.CharField(max_length=1, null=True)

    def __str__(self):
        first = f", {self.first_initial}." if self.first_initial else ""
        middle = f", {self.middle_initial}." if self.middle_initial else ""
        return f"{self.name}" + first + middle


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

    def __str__(self):
        return f"{self.index}: {self.title[:15]}... "


class Questionnaire(models.Model):
    
    # index = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.URLField(null=True)
    description = models.CharField(max_length=1500)
    abbreviation = models.CharField(max_length=50)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)
    year = models.PositiveIntegerField()
    use_with_assessments = models.ManyToManyField('self', blank=True)
    indices_reference = models.ForeignKey(Reference, null=True, on_delete=models.SET_NULL)
    # ANIRUDH: LEFT column
    index_license = models.PositiveIntegerField(null=True) #change to foreign keys at a later date
    index_language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    # indices_language_not_in_mhdb = models.ManyToManyField(Language) # exclude for now, indicates languages that the assessment is available in but which have not been added to mindlogger.
    # LEFT column errors                
    indices_respondent = models.ManyToManyField('Respondent', blank=True)    # need to find this table in the spreadsheets
    indices_subject = models.ManyToManyField('Subject', blank=True)       # need to find this table in the spreadsheets
    age_min = models.PositiveSmallIntegerField(null=True)
    age_max = models.PositiveSmallIntegerField(null=True)
    number_of_questions = models.PositiveSmallIntegerField(null=True)
    number_of_questions_with_ranges = models.PositiveIntegerField(null=True)
    minutes_to_complete = models.PositiveIntegerField(null=True)
    minutes_to_complete_with_ranges = models.CharField(null=True, max_length=10)
    indices_age = models.ManyToManyField('Age', blank=True) # need to find this table in the spreadsheets
    indices_disorder = models.ManyToManyField(DisorderCategory, blank=True)
    # indices_disorder_category         # this field in the the disorder table
    # ANIRUDH: LEFT column.1
    # ANIRUDH: RIGHT column
    # indices_disorder_subcategory      # this field in the the disorder table
    # indices_disorder_subsubcategory   # this field in the the disorder table

    def __str__(self):
        return f"{self.id}: {self.title[:15]}... "

class Question(models.Model):
    
    # index = models.IntegerField()
    text = models.CharField(max_length=200)
    questionaires = models.ManyToManyField(Questionnaire) #https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-many-relationships

    def __str__(self):
        return f"{self.index}: {self.text[:15]}... "
