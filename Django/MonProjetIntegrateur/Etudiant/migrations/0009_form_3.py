# Generated by Django 4.2.1 on 2023-06-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0008_form_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sept_heure', models.CharField(db_column='sept_heure', max_length=40)),
                ('huit_heure', models.CharField(db_column='huit_heure', max_length=40)),
                ('neuf_heure', models.CharField(db_column='neuf_heure', max_length=40)),
                ('dix_heure', models.CharField(db_column='dix_heure', max_length=40)),
                ('onze_heure', models.CharField(db_column='onze_heure', max_length=40)),
                ('douze_heure', models.CharField(db_column='douze_heure', max_length=40)),
                ('treize_heure', models.CharField(db_column='treize_heure', max_length=40)),
                ('quatorze_heure', models.CharField(db_column='quatorze_heure', max_length=40)),
                ('quinze_heure', models.CharField(db_column='quinze_heure', max_length=40)),
                ('seize_heure', models.CharField(db_column='seize_heure', max_length=40)),
                ('dix_sept_heure', models.CharField(db_column='dix_sept_heure', max_length=40)),
                ('dix_huit_heure', models.CharField(db_column='dix_huit_heure', max_length=40)),
                ('dix_neuf_heure', models.CharField(db_column='dix_neuf_heure', max_length=40)),
            ],
        ),
    ]