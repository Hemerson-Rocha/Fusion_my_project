# Generated by Django 4.1.7 on 2023-02-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(max_length=100, verbose_name='Cargo'),
        ),
    ]
