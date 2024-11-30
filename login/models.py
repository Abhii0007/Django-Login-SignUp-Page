from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Adjust length for your needs
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in production

    def __str__(self):
        return self.name
