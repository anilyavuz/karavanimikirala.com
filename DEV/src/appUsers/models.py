from django.db import models

# Create your models here.userID(primary key)
import uuid


class AppUser(models.Model):
    appUserId = models.CharField(
        max_lenght=100, null=True, blank=True, Unique=True, default=uuid.uuid4)

    email = models.EmailField(min_lenght=5, blank= False, null= False)
    name = models.TextField(blank=False, null=False)
    lastName = models.TextField(blank=False, null=False)
    password = models.CharField(min_lenght=8, blank=False, null=False)
    productAmount = models.IntegerField(blank=True, null=True)
    rentedProductAmount = models.IntegerField(blank=True, null=True)
