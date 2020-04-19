from django import forms

from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answerId',
            'replyEntryDate',
            'replyContent',
            'replierUserId',
            'questionId'
        ]