# Generated by Django 3.2.16 on 2023-01-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20230110_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='flats', to='property.Flat', verbose_name='Квартира в собственности'),
        ),
    ]