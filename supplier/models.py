from django.db import models


class Supplier(models.Model):
    # Campos básicos del proveedor
    business_name = models.CharField(max_length=255)
    nit = models.PositiveIntegerField()
    tax_responsibility = models.CharField(max_length=255)
    taxpayer_type = models.CharField(max_length=255)
    responsibility_type = models.CharField(max_length=255)

    # Campos de localización
    country = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)

    # Campos de contacto
    billing_email = models.EmailField()
    sales_contact = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
