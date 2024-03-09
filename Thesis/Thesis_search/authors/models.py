from django.db import models

class Thesis(models.Model):
  firstname = models.CharField(max_length=255, default='')
  lastname = models.CharField(max_length=255, default='')
  research_title = models.CharField(max_length=255, default='')
  abstract = models.TextField(default='')