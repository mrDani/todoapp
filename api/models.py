from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    class Meta:
        db_table='task'
  
    def __str__(self):
        return self.title
        