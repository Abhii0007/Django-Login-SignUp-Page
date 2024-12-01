import os,django,time
import pandas
from login.models import User

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
django.setup()


users = User.objects.values()

print(pandas.DataFrame(list(users)))


#for user in users:
#    print(f"Name: {user.name}, Phone: {user.phone}, Email: {user.email},password:{user.password}")