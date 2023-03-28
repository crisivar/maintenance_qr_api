import uuid
from django.db import models
from activity.models import Activity
from category.models import SubCategory


class EquipmentMaintenance(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='maintenance/', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)
    pending = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.activity.code:
            self.activity.code = self.generate_code()
            self.activity.save()
        super(EquipmentMaintenance, self).save(*args, **kwargs)

    def generate_code(self):
        # Use UUID to generate a unique code
        code = str(uuid.uuid4().hex)[:10]
        return code
