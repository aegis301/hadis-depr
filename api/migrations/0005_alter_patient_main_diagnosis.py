# Generated by Django 4.0.2 on 2022-02-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_patient_created_at_remove_patient_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='main_diagnosis',
            field=models.CharField(max_length=1000),
        ),
    ]
