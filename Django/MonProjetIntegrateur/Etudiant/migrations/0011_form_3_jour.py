# Generated by Django 4.2.1 on 2023-06-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0010_verification0'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_3',
            name='jour',
            field=models.CharField(db_column='jour', default=0, max_length=40),
            preserve_default=False,
        ),
    ]
