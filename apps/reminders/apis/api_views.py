from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from reminders.serializers import ReminderSerializer
from reminders.models import Reminder

class ReminderAPIView(GenericAPIView):

    """ API for getting or creating reminders """

    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    
    def get(self, request, *args, **kwargs):
        reminders = self.queryset.filter(user=request.user)
        data = self.serializer_class(reminders,many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)