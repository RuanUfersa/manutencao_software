# Generated by Django 5.0.4 on 2024-04-18 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frutas',
            options={'verbose_name': 'Fruta', 'verbose_name_plural': 'Frutas'},
        ),
        migrations.AlterModelOptions(
            name='verduras',
            options={'verbose_name': 'Verdura', 'verbose_name_plural': 'Verduras'},
        ),
    ]
