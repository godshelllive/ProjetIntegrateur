# Generated by Django 4.2.1 on 2023-06-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0004_form_1_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_1',
            name='bool',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
