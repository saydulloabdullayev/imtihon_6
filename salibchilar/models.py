from django.db import models

class Salib(models.Model):
    nomi = models.CharField(max_length=100)
    yil = models.IntegerField()
    tavsif = models.TextField()

class Theme(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()



    def __str__(self):
        return self.nomi
