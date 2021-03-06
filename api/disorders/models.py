from django.db import models

class Icd9Cm(models.Model):
    icd9cm = models.CharField(max_length=50)

class Icd10Cm(models.Model):
    icd10cm = models.CharField(max_length=50)

class EquivalentClass(models.Model):
    
    pass


class Severity(models.Model):

    severity = models.CharField(max_length=50)
    definition = models.CharField(max_length=200)
    equivalent_classes = models.CharField(max_length=500, null=True)
    # subClassOf

class DisorderCategory(models.Model):

    name = models.CharField(max_length=200)
    # ICD9CM = models.ManyToManyField('ICD9CM')
    # ICD10CM = models.ManyToManyField('ICD10CM')

    def __str__(self):
        return self.name


class DiagnosticSpecifier(models.Model):

    diagnostic_specifier = models.CharField(max_length=200)
    equivalent_classes = models.CharField(max_length=500)


class DiagnosticCriterion(models.Model):

    diagnostic_criterion = models.CharField(max_length=200) 
    equivalent_classes = models.CharField(max_length=500)


class Disorder(models.Model):

    index_disorder_category = models.ForeignKey(DisorderCategory, on_delete=models.CASCADE)
    #  'index_disorder_subcategory',
    #  'index_disorder_subsubcategory',
    #  'index_disorder_subsubsubcategory',
    disorder = models.CharField('name of the disorder', max_length=200)
    equivalent_classes = models.ManyToManyField('EquivalentClass')
    icd9cm = models.CharField(max_length=100, null=True) # needs to be changed to a ManyToManyField
    icd10cm = models.CharField(max_length=100, null=True) # needs to be changed to a ManyToManyField
    index_diagnostic_specifier = models.ForeignKey(DiagnosticSpecifier, null=True, on_delete=models.SET_NULL)
    #  'index_diagnostic_inclusion_criterion',
    #  'index_diagnostic_inclusion_criterion2',
    #  'index_diagnostic_exclusion_criterion',
    #  'index_diagnostic_exclusion_criterion2',
    index_severity = models.ForeignKey(Severity, null=True, on_delete=models.SET_NULL)
    note = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.disorder