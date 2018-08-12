from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Cublista(models.Model):
    """This class represents the bucketlist model."""
    projeto = models.CharField(max_length=255, blank=False)
    tipo = models.CharField(max_length=255, blank=False)
    padrao = models.CharField(max_length=255, blank=False)
    estado = models.CharField(max_length=255, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=4)
    mes = models.CharField(max_length=255, blank=False)
    ano = models.IntegerField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.projeto)

