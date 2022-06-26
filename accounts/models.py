from cmath import phase
from pyexpat import model
from django.db import models
from django.forms import ValidationError
from sqlalchemy import delete

class Project(models.Model):
    STATUS = (
        ('Inititated', 'Inititated'),
        ('Paused', 'Paused'),
        ('In progress', 'In progress'),
        ('Aborted', 'Aborted'),
        ('Completed', 'Completed')
    )

    PHASE = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10,"10")
    )

    project_name = models.CharField(max_length=100, null=True)
    client_name = models.CharField(max_length=100, null=True)
    client_mail = models.CharField(max_length=100, null=True)
    project_initiated_on = models.DateField(null=True)
    ect = models.DateField(null=True)
    project_status = models.CharField(max_length=200,null=True, choices=STATUS, default='Initiated')
    collaborations = models.IntegerField(null=True, default=0)
    phase = models.IntegerField(null=True,choices=PHASE, default=1)
    
    def __str__(self):
        return self.p_name

    @property
    def phase_percentage(self):
        return self.phase * 10