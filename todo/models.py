from django.db import models
from django.urls import reverse


class Tarea(models.Model):
    tarea = models.CharField(max_length=100)

 #   def __str__(self):
 #       return self.tarea

class Projects(models.Model):
    company = models.CharField(max_length=100)
    description = models.TextField()
    program = models.CharField(max_length=100)
    generated_deca = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('generardoc', args=[str(self.id)])

