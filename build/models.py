from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    

    
class Ourblog(models.Model):
    image =models.ImageField(upload_to='images')
    text =models.TextField()
    body= models.TextField()

    def __str__(self) -> str:
        return self.text


class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message =models.TextField()

    def __str__(self) -> str:
        return self.first_name


# qo'shimcha modellar
class Partner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    
class Activitie(models.Model):
    image =models.ImageField(upload_to='images')
    title =models.CharField(max_length=255)
    body =models.TextField()

    def __str__(self) -> str:
        return self.title