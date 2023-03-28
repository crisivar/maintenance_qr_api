from django.db import models
from client.models import Client
from laboratory.models import Laboratory
from responsible_person.models import ResponsiblePerson
from equipment.models import Equipment


class Activity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    responsible_person = models.ForeignKey(
        ResponsiblePerson, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField()
    code = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
