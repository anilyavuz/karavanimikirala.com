from django.db import models

# Create your models here.userID(primary key)
import uuid


class User(models.Model):
    userId = models.CharField(
        max_lenght=100, null=True, blank=True, Unique=True, default=uuid.uuid4)

    mail = models.EmailField(min_lenght=5, blank= False, null= False)
    name = models.TextField(blank=False, null=False)
    Lastname = models.TextField(blank=False, null=False)
    Password = models.CharField(min_lenght=8, blank=False, null=False)
    productamount = models.IntegerField(blank=True, null=True)
    Rentedproductamount = models.IntegerField(blank=True, null=True)
