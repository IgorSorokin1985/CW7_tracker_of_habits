from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """Paginator for habits"""
    page_size = 5
