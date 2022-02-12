# Generated by Django 4.0.2 on 2022-02-10 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_alter_patient_main_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]