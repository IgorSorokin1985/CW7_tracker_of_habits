from rest_framework.routers import DefaultRouter
from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitListAPIView, HabitDestroyAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitCreateAPIView
# Описание маршрутизации для ViewSet

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='lesson_create'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='lesson_delete'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='lesson_update'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='lesson_detail'),
    path('habit/', HabitListAPIView.as_view(), name='lesson_list'),
]
