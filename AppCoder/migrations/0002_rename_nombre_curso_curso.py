# Generated by Django 4.0.4 on 2022-05-28 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nombre',
            new_name='curso',
        ),
    ]