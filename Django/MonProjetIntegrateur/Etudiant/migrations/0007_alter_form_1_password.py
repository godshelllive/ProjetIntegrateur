# Generated by Django 4.2.1 on 2023-06-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0006_remove_form_1_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_1',
            name='password',
            field=models.CharField(max_length=18),
        ),
    ]