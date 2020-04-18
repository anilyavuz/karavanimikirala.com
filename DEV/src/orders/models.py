from django.db import models

# Create your models here.

#class Order(models,Model):


''' 1 - Peer to peer system
2 - Also big brands can join

1 - User Profile
userID(primary key)
mail
Name
Lastname
Password
productamount
Rentedproductamount

2 - Products 
ProductID
productType
userID(fk)
productName
ProductVerification(bool)
ProductLicense

3.Carmodels
modelid
Brandid
Brandname
Size
4.extras


3.orders
Productid
ownerUserid
Orderid
Renteruserid
Orderstartdate
Orderenddate

3.questionEntries
questionEntryid user_id(fk)
Question string

4.answerentries
Answerentryid
replierUserid
Questionentryid
Askeruserid
Answer string
 '''