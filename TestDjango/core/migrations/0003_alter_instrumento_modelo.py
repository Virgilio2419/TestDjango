# Generated by Django 4.2.13 on 2024-06-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_instrumento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='modelo',
            field=models.CharField(max_length=100),
        ),
    ]
