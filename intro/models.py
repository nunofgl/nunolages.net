from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=150)
