# Generated by Django 5.1.4 on 2025-04-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_patient_age_alter_patient_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.AddField(
            model_name='patient',
            name='Gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('O', 'Other'), ('X', 'Prefer not to say')], default='X', max_length=2, verbose_name='Gender'),
        ),
    ]
