# Generated by Django 4.2.1 on 2023-06-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0011_form_3_jour'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lundi', models.CharField(db_column='lundi', max_length=1000000)),
                ('mardi', models.CharField(db_column='mardi', max_length=1000000)),
                ('mercredi', models.CharField(db_column='mercredi', max_length=1000000)),
                ('jeudi', models.CharField(db_column='jeudi', max_length=1000000)),
                ('vendredi', models.CharField(db_column='vendredi', max_length=1000000)),
                ('samedi', models.CharField(db_column='samedi', max_length=1000000)),
            ],
        ),
    ]
