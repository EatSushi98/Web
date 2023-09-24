from django.db import models

# Create your models here.

class Contact(models.Model):
    Name=models.CharField(max_length=122)
    Phone=models.CharField(max_length=12)
    Date=models.DateField()

def __str__(self):
    return self.name + self.phone




