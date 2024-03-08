from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitListAPIView, HabitDestroyAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitCreateAPIView, HabitsPublicListAPIView
# Описание маршрутизации для ViewSet

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/', HabitListAPIView.as_view(), name='own_habits_list'),
    path('habit/public/', HabitsPublicListAPIView.as_view(), name='public_habits_list'),
]
