import os
import django

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
django.setup()

from login.models import User

# Fetch all user data
users = User.objects.all()

# Print user data
for user in users:
    print(f"Name: {user.name}, Phone: {user.phone}, Email: {user.email},password:{user.password}")
