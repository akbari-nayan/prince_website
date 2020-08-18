from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    name     = models.CharField(max_length=30,default='')
    email    = models.EmailField(max_length=254,blank=True)
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    contact  = PhoneNumberField(blank=True)
    city     = models.CharField(max_length=30,blank=True)
    created  = models.DateTimeField(auto_now=True)
    updated  = models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        return f"{self.user} -- {self.created.strftime('%d-%m-%y')}"

    def save(self, *args, **kwargs):
        self.name = str(self.user)
        super().save(*args, **kwargs)


class Contact(models.Model):

    name     = models.CharField(max_length=30)
    contact  = PhoneNumberField(blank=True)
    city     = models.CharField(max_length=30,blank=True)
    message  = models.TextField(max_length=2000) 
    created  = models.DateTimeField(auto_now=True)
    updated  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.name} -- {self.created.strftime('%d-%m-%y')}"




