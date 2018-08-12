from django.db import models

class ProjPadrao(models.Model):
    #name = models.CharField(max_length=30, unique=True)
    #description = models.CharField(max_length=100)
    estado=models.CharField(max_length=2)
    tipo=models.IntegerField()
    area=models.DecimalField(max_digits=6, decimal_places=2)
    num_pavimentos=models.IntegerField()
    padrao=models.IntegerField()

    def __str__(self):
        return str(self.id)
    