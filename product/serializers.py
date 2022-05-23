from rest_framework import serializers

from .models import Product, Comment, Category



class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""
    class Meta:
        model = Comment
        exclude = ( 'create_at', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        print(request)
        representation['user'] = request.user.email
        return representation


class CommentSerializer(serializers.ModelSerializer):
    """Вывод отзыво"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("user", "text", "children")

class CommentRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'description', 'price', 'image', 'comment')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'