# Generated by Django 4.1.5 on 2023-11-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_patientprofile_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='bloodgroup',
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='certificate',
            field=models.FileField(upload_to=''),
        ),
    ]
