# your_app/migrations/0005_create_superuser.py

from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@example.com',
            password=make_password('adminpassword'),
            is_staff=True,
            is_superuser=True
        )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_orderitem_product_delete_product'),  # Adjust to your latest migration dependency
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
