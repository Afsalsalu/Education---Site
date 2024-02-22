from django.db import models

# Create your models here.

class Teachers(models.Model):
    image=models.ImageField(upload_to='imgs')
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    rating=models.FloatField()
    facebook=models.CharField(max_length=999)
    twitter=models.CharField(max_length=999)
    whatsapp=models.CharField(max_length=999)
    instagram=models.CharField(max_length=999)

    def __str__(self):
     return self.name
    

class Blog(models.Model):
    image=models.ImageField(upload_to='imgs')
    Date=models.DateField()
    User=models.CharField(max_length=50)
    Phara=models.TextField()
    
    def __str__(self):
     return self.User
    


class Contacts(models.Model):
   address=models.TextField()
   name=models.CharField(max_length=50)
   state=models.CharField(max_length=50)
   email=models.EmailField(max_length=50)
   mobile=models.CharField(max_length=50)
    


