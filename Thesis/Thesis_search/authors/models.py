from django.db import models

class Thesis(models.Model):
    firstname = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    abstract = models.TextField(default='')

def __str__(self):
    return f"{self.firstname} {self.lastname}"