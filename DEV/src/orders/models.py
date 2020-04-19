from django.db import models

import uuid

from ..appUsers.models import AppUser as appUser_model

from ..products.models import Product as product_models

class Order(models.Model):

 orderId = models.CharField(max_lenght=100, null=True, blank=True, Unique= True, default=uuid.uuid4)
 orderStartDate = models.DateField(blank=False, null=False)
 orderEndDate = models.DateField(blank=False, null=False)

#foreign keys

 ownerUserId = models.ForeignKey(appUser_model.appUserId)
 renterUserId = models.ForeignKey(appUser_model.appUserId)
 productId = models.ForeignKey(product_models.ProductID) 


