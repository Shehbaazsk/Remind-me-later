from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Reminder(models.Model):
    class RemindMode:
        SMS = 'sms'
        EMAIL = 'email'
        # Add more modes
        choices = [
            (SMS,'sms'),
            (EMAIL,'email'),
            # Add more modes
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reminder")
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    # HERE WE CAN EITHER SAVE DATE AND TIME SEPARATELY OR IN THE SAME FIELD AS WISHED

    # date_time = models.DateTimeField()
    

    remind_mode = models.CharField(max_length=20, choices=RemindMode.choices, default=RemindMode.EMAIL)