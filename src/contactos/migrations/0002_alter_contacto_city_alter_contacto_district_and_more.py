# Generated by Django 4.0.5 on 2022-06-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='district',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]