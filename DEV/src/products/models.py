from django.db import models

# Create your models here.
class Product(models.Model):
    ProductID
    productType
    userID(fk)
    productName 
    ProductVerification(bool)
    ProductLicense 
