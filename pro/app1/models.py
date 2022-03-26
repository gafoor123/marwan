from django.db import models

class reg(models.Model):
    Name = models.CharField(max_length=80)
    Roll_no = models.IntegerField()
    Age = models.IntegerField()

class login(models.Model):
    Username = models.CharField(max_length=70)
    Password = models.CharField(max_length=70)


