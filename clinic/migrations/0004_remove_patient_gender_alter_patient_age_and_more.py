# Generated by Django 5.1.4 on 2025-04-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_remove_patient_gender_patient_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Gender',
        ),
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=10, verbose_name='Gender'),
        ),
    ]
