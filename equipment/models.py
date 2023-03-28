from django.db import models
from client.models import Client
from laboratory.models import Laboratory
from responsible_person.models import ResponsiblePerson


class Equipment(models.Model):
    image = models.ImageField(upload_to='equipments/', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    responsible_person = models.ForeignKey(
        ResponsiblePerson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    billing_internal_code = models.CharField(max_length=50)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    minimum_inventory = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
