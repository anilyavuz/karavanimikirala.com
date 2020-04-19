from django.db import models
import uuid
from DEV.src.appUsers.models import AppUser as appUser_models
from datetime import date

class Question(models.Model):

 questionId = models.CharField(
     max_lenght=100, null=True, blank=True, Unique=True, default=uuid.uuid4)
 questionEntryDate = models.DateTimeField(date.today)
 questionContent = models.TextField(blank= True, null=True, max_length=250)

#foreign keys

 askerUserId = models.ForeignKey(appUser_models.appUserId)


