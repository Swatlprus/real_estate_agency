# Generated by Django 3.2.16 on 2022-12-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Нормализованный номер владельца'),
        ),
    ]
