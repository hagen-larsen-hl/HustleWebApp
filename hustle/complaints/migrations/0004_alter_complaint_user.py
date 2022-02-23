# Generated by Django 4.0.2 on 2022-02-23 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaints', '0003_alter_complaint_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
