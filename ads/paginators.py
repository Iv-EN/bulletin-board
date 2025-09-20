from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class BasePaginator(PageNumberPagination):
    page_size_query_param = "page_size"

    def __init__(self, page_size_setting, max_page_size_setting):
        self.page_size = getattr(settings, page_size_setting)
        self.max_page_size = getattr(settings, max_page_size_setting)


class AdsPaginator(BasePaginator):
    def __init__(self):
        super().__init__(
            "PAGINATOR_ADS_PAGE_SIZE", "PAGINATOR_ADS_MAX_PAGE_SIZE"
        )
