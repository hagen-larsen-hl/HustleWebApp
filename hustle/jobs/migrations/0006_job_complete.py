# Generated by Django 3.2.6 on 2022-02-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_job_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
