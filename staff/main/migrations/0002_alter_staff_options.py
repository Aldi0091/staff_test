# Generated by Django 4.0.6 on 2022-07-13 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'an employee', 'verbose_name_plural': 'Employees'},
        ),
    ]