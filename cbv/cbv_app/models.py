from django.db import models
from django.shortcuts import reverse

class School(models.Model):
    name = models.CharField(max_length=250)
    principle = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cbv_app:detail', kwargs={'pk':self.pk})

class Students(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name