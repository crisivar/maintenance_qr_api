# Generated by Django 4.1.7 on 2023-03-29 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='maintenance/')),
                ('observations', models.TextField(blank=True, null=True)),
                ('pending', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory')),
            ],
        ),
    ]