import os,django,time
import pandas


# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
django.setup()

from login.models import User
users = User.objects.values()
#for user in users:
#    print(f"Name: {user.name}, Phone: {user.phone}, Email: {user.email},password:{user.password}")




print(pandas.DataFrame(list(users)))
