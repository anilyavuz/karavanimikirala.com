from django.db import models

import uuid

# Create your models here.
class Product(models.Model):
    ProductID = models.CharField(max_lenght=100, null=True, blank=True, Unique=True, default=uuid.uuid4)
    productType = models.TextField(blank=True, null=True)
    productName = models.TextField(blank=False, null=False)
    ProductVerification = models.BooleanField(default=False)
    ProductLicense = models.TextField(blank= True, null=True)
    
    #foreign keys
    
    #userId = models.ForeignKey(User.userId) #wtf
    
    userId = models.ForeignKey(
        related_name="User",
        verbose_name = ("userId")
    )
    
    
