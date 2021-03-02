from django.db import models

class Language(models.Model):

    # index = models.PositiveIntegerField()
    name = models.CharField(max_length=100 )
    parent_language = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    equivalent_classes = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"
