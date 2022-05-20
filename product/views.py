from rest_framework import viewsets, pagination, filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class MyPaginationView(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPaginationView

    search_fields = ('title', 'description', )
    filter_backends = (filters.SearchFilter, )

    @action(detail=False, methods=['get'])
    def filter(self, request):
        queryset = self.queryset

        price = request.query_params.get('price')
        category = request.query_params.get('category')
        print(request.query_params)
        if category:
            queryset = queryset.filter(category=category)
        elif price == 'asc':
            queryset = queryset.order_by('price')
        elif price == 'desc':
            queryset = queryset.order_by('-price')

        # разбиваем queryset на страницы
        page = self.paginate_queryset(queryset)
        # сериализуем
        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)