from rest_framework import serializers
from women.models import Women, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class WomenSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Women
        fields = ('title', 'category_id')
