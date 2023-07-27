# user_management/models.py
from django.db import models

class SecurityQuestion(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    security_question = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    security_answer = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username
