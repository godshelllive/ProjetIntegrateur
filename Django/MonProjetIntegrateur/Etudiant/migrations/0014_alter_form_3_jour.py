# Generated by Django 4.2.1 on 2023-06-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0013_alter_form_3_dix_heure_alter_form_3_dix_huit_heure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_3',
            name='jour',
            field=models.CharField(db_column='jour', max_length=8),
        ),
    ]