# core/migrations/0006_auto_20240717_0524.py

import os
from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    # Get the custom user model
    CustomUser = apps.get_model('users', 'CustomUser')
    if not CustomUser.objects.filter(username='admin').exists():
        CustomUser.objects.create(
            username='admin',
            email=os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'),
            password=make_password(os.getenv('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')),
            is_staff=True,
            is_superuser=True
        )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20240717_0524'),  # Adjust to your latest migration dependency
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
