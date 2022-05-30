from cmath import phase
from pyexpat import model
from django.db import models

# Phases table 
class Phase(models.Model):
    phase = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.phase

# Projects table 
class Project(models.Model):
    STATUS = (
        ('Inititated', 'Inititated'),
        ('Paused', 'Paused'),
        ('In progress', 'In progress'),
        ('Aborted', 'Aborted'),
        ('Completed', 'Completed')
    )

    p_id = models.IntegerField(null=True)
    p_name = models.CharField(max_length=100, null=True)
    c_name = models.CharField(max_length=100, null=True)
    c_mail = models.CharField(max_length=100, null=True)
    init_date = models.DateField(null=True)
    ect = models.DateField(null=True)
    status = models.CharField(max_length=200,null=True, choices=STATUS)
    collabs = models.IntegerField(null=True)
    phase = models.ManyToManyField(Phase)

    def __str__(self):
        return self.p_name