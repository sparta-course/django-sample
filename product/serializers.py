from rest_framework import serializers

from user.models import User as UserModel
from user.models import Celler as CellerModel
from user.models import Cart as CartModel
from user.models import PurchaseList as PurchaseListModel
from user.models import PurchaseHistory as PurchaseHistoryModel

from product.models import Product as ProductModel
from product.models import ProductOption as ProductOptionModel
from product.models import Review as ReviewModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["id", "user", "title", "description", "created",]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ["product", "user", "rating", "content", "created"]

        extra_kwargs = {
            "product": {"write_only": True},
        }


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionModel
        fields = ["name", "price"]
    

class ProductDetailSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, source="productoption_set")
    reviews = ReviewSerializer(many=True, source="review_set")

    class Meta:
        model = ProductModel
        fields = ["user", "title", "description", "created", "options", "reviews"]