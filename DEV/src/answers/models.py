from django.db import models
import uuid
from .models import AppUser as appUser_models
from .models import Question as question_models
from datetime import date


class Answer(models.Model):

    answerId = models.CharField(
    max_lenght=100, null=True, blank=True, Unique=True, default=uuid.uuid4)
    replyEntryDate = models.DateTimeField(date.today)
    replyContent = models.TextField(blank=True, null=True, max_length=250)

    #foreign keys

   # replierUserId = models.ForeignKey(appUser_models.app)
    questionId = models.ForeignKey(question_models.questionId)
    