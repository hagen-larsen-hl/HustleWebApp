# Generated by Django 4.0.2 on 2022-03-15 18:42

from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from jobs.models import Job
from jobs.models import JobType


def seed_permissions(apps, schema_editor):
    pass
    #job_content_type = ContentType.objects.get_for_model(Job)
    #can_create = Permission.objects.create(name="Can Create Job", codename="can_create", content_type=job_content_type)
    #Group.objects.get(name="Customer").permissions.add(can_create)

def remove_permissions(apps, schema_editor):
    pass
    #Permission.objects.get(name="Can Create Job").delete()

def seed_job_types(apps, schema_editor):
    JobType.objects.create(type="Mow Lawn")
    JobType.objects.create(type="Shovel Snow")
    JobType.objects.create(type="Rake Leaves")

def remove_job_types(apps, schema_editor):
    JobType.objects.get(type="Mow Lawn").delete()
    JobType.objects.get(type="Shovel Snow").delete()
    JobType.objects.get(type="Rake Leaves").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_seed'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_permissions, remove_permissions),
        migrations.RunPython(seed_job_types, remove_job_types),
    ]
