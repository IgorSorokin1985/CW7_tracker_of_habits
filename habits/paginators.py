from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """Paginator for habits"""
    page_size = 5


class NiceHabitsPagination(PageNumberPagination):
    """Paginator for nice habits"""
    page_size = 5
