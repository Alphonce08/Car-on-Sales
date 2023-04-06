from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    phonenumber = models.IntegerField(blank=False, null=False)
    carname = models.CharField(max_length=30, blank=False, null=False, default=3)
    date = models.IntegerField(blank=False, null=False)
    client = models.CharField(max_length=30, blank=False, null=False)
    phonenum = models.IntegerField(blank=False, null=False)

def __str__(self):
    return self.name

