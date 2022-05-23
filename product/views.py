from rest_framework import viewsets, pagination, filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Product, Comment
from .serializers import ProductSerializer, CommentCreateSerializer, CommentRetrieveUpdateDestroySerializer
from .helpers import MyPaginationView, IsAdminOrReadOnly, IsOwnerOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPaginationView
    permission_classes = (IsAdminOrReadOnly,)

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

        """ разбиваем queryset на страницы """
        page = self.paginate_queryset(queryset)
        """ сериализуем """
        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        return {'request': self.request,
                'format': self.format_kwarg,
                'view': self}



class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveUpdateDestroySerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly,)




    # """Добавление отзыва к фильму"""
    # def post(self, request):
    #     comment = CommentCreateSerializer(data=request.data)
    #     print(comment)
    #     if comment.is_valid(raise_exception=True):
    #         comment.save()
    #     return Response( status=201)