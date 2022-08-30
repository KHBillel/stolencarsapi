from django.db import models

# Create your models here.


class Vehicule(models.Model) :
    mat =  models.TextField(unique=True)
    nc = models.TextField(primary_key=True)
    vbrand = models.TextField()
    vmodel = models.TextField()
    current_location =  models.TextField(null=True, blank=True)
    isStolen =  models.BooleanField(default=False)
    short_description = models.TextField()

    def __str__(self) :
        return self.vbrand + " " + self.vmodel + " " + self.mat + " " + self.short_description
