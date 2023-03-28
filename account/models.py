from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField



# Create your models here.
class Address(models.Model):
    country = CountryField()
    state = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    build = models.CharField(max_length=128)
    zip = models.CharField(max_length=6)

    def __str__(self):
        return self.city + ", " + self.state + ", " + self.zip + "," + self.street + "," + self.build

class Customer(AbstractUser):
    photo = models.ImageField(upload_to="users/photo/%Y", blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    discount = models.IntegerField(default=0)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)
    is_temp = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.username
    
    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return "/static/img/no_avatar.png"
    
    


