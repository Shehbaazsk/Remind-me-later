from django.urls import path
from reminders.apis.api_views import ReminderAPIView

app_name = 'reminders'

urlpatterns = [
    path('reminder/', ReminderAPIView.as_view(), name='reminder'),
]
