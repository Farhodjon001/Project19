from django.db import models

# Create your models here.
class Pupil(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
    birh_date=models.DateField()
    grade=models.IntegerField()