from django.db import models

class displaydata(models.Model):
    Cname = models.CharField(max_length=200)
    Sname = models.CharField(max_length=200)
