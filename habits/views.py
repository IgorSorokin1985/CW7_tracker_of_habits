from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from habits.models import Habit
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner
from habits.serializers import HabitSerializer, HabitsSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
#from materials.utils import get_url_for_payment


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    #pagination_class = MaterialsPagination

    def get_queryset(self):
        list_habits = super().get_queryset()
        return list_habits.filter(user=self.request.user)


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all().filter(is_public=True)
    permission_classes = [IsAuthenticated]
    #pagination_class = MaterialsPagination

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
