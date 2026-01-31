from rest_framework import serializers
from .models import Userprofile, Category, Store, Product, Order, Review, Contact, Address, StoreMenu
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ('id', 'username', 'email', 'password', 'role', 'phone_number', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}  # Пароль нельзя будет прочитать через API
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return super(UserSerializer, self).create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='category_name', queryset=Category.objects.all())

    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')

    class Meta:
        model = Order
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'