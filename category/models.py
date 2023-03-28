from django.db import models


class Category(models.Model):
    # Campos de la categoría principal
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    # Campo para relacionar con la categoría principal
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Campos de la subcategoría
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
