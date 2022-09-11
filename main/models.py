from django.db import models

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    Role = (
        ('admin', 'admin'),
        ('owner', 'owner'),
    )
    
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=Role)
    
    
    washCompany = models.ForeignKey('WashCompany', on_delete=models.CASCADE, null=True)
    
    

class WashCompany(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='washCompany_images/', blank=True, null=True)
    location = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
    
class Washer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    stake = models.IntegerField()
    image = models.ImageField(upload_to='washer_images/')
    is_active = models.BooleanField()
    
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    washCompany = models.ForeignKey(WashCompany, on_delete=models.CASCADE)
    


class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()
    
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    washCompany = models.ForeignKey(WashCompany, on_delete=models.CASCADE)
    
    
class Order(models.Model):
    price = models.IntegerField()
    car_model = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    car_number = models.IntegerField()
    client_number = models.IntegerField()
    is_active = models.BooleanField()
    is_cancelled = models.BooleanField()
    date = models.DateField()
    
    
    washCompany = models.ForeignKey(WashCompany, on_delete=models.CASCADE)



class Journal(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    previousCarModel = models.CharField(max_length=255)
    currentCarModel = models.CharField(max_length=255)
    previousCarNumber = models.CharField(max_length=255)
    currentCarNumber = models.CharField(max_length=255)
    previousService = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='previous_service')
    currentService = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='current_service')
    cancelledReason = models.CharField(max_length=255)