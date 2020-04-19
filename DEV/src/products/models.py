from django.db import models

import uuid

from DEV.src.users.models import User as user_models 

# Create your models here.
class Product(models.Model):
    ProductID = models.CharField(max_lenght=100, null=True, blank=True, Unique=True, default=uuid.uuid4)
    productType = models.TextField(blank=True, null=True)
    productName = models.TextField(blank=False, null=False)
    productVerification = models.BooleanField(default=False)
    productLicense = models.TextField(blank= True, null=True)
    
    #foreign keys
    user_id = models.ForeignKey(user_models.userId) 

    
