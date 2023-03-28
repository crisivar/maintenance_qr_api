from django.db import models
from client.models import Client


class Laboratory(models.Model):
    # Campo para seleccionar el cliente
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    # Campos del laboratorio
    laboratory_name = models.CharField(max_length=255)
    responsible_person = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.laboratory_name
