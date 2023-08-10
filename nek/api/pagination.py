from rest_framework.pagination import PageNumberPagination


class CustomPostPagination(PageNumberPagination):
    """Параметр пагинации при запросе."""

    page_size = 10
