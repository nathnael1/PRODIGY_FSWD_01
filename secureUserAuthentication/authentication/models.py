from django.db import models

class user(models.Model):
    fullName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


