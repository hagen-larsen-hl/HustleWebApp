# Generated by Django 3.2.6 on 2022-02-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobtype_type_alter_job_customer_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='time_estimate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='type',
            field=models.CharField(default='Mow Lawn', max_length=30),
        ),
    ]
