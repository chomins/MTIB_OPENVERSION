from django.db import models

# Create your models here.

class Complain(models.Model):
    complain_id = models.AutoField(primary_key = True, unique=True)
    complain = models.CharField(max_length=300)