from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class EdificacionPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'

class EdificacionLOPagination(LimitOffsetPagination):
    default_limit = 1