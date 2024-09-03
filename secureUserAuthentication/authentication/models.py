from django.db import models

class user(models.Model):
    password = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()

