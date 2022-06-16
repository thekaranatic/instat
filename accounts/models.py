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

    p_name = models.CharField(max_length=100, null=True)
    c_name = models.CharField(max_length=100, null=True)
    c_mail = models.CharField(max_length=100, null=True)
    init_date = models.DateField(null=True)
    ect = models.DateField(null=True)
    status = models.CharField(max_length=200,null=True, choices=STATUS)
    collabs = models.IntegerField(null=True)
    phase = models.IntegerField(null=True,choices=PHASE)
    
    def __str__(self):
        return self.p_name

    @property
    def phase_percentage(self):
        return self.phase * 10