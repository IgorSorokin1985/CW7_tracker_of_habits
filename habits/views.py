from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from habits.models import Habit
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModerator, IsOwner
from habits.serializers import HabitSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
#from materials.utils import get_url_for_payment


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    #permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    #pagination_class = MaterialsPagination


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    #permission_classes = [IsAuthenticated, IsModerator | IsOwner]
