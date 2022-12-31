# Generated by Django 3.2.16 on 2022-12-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20221226_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', models.CharField(max_length=20, verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(related_name='owner_flats', to='property.Flat', verbose_name='Квартира в собственности')),
            ],
        ),
    ]