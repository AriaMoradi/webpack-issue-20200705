from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import User  # where User lives
import os  # env var access


def forwards(apps, schema_editor):
    # build the user you now have access to via Django magic
    User.objects.create_superuser(username=settings.SUPERUSER_USERNAME,
                                  password=settings.SUPERUSER_PASSWORD)


def reverse(apps, schema_editor):
    User.objects.get(username=settings.SUPERUSER_USERNAME).delete()


# destroy what forward_func builds
class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial')
    ]
    operations = [
        migrations.RunPython(forwards, reverse),
    ]
