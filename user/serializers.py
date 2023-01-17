from dataclasses import field
from rest_framework import serializers

from user.models import User as UserModel
from user.models import Celler as CellerModel
from user.models import Cart as CartModel
from user.models import PurchaseList as PurchaseListModel
from user.models import PurchaseHistory as PurchaseHistoryModel

from product.serializers import ProductOptionSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password",
                  "fullname", "phone", "cart", "like", ]

        read_only_fields = ["like", "cart", ]

        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop("password", "")
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()

        return user

class UserCartSerializer(serializers.ModelSerializer):
    product_option_id = serializers.IntegerField(write_only=True)
    product_info = serializers.SerializerMethodField(read_only=True)

    def get_product_info(self, obj):
        return obj.product_option.product.title

    product_option_info = serializers.SerializerMethodField(read_only=True)
    def get_product_option_info(self, obj):
        return obj.product_option.name

    price = serializers.SerializerMethodField(read_only=True)
    sum_price = serializers.SerializerMethodField(read_only=True)
    def get_price(self, obj):
        return obj.product_option.price

    def get_sum_price(self, obj):
        return obj.product_option.price * obj.count

    class Meta:
        model = CartModel
        fields = ["user", "count", "product_option_id",
         "product_info", "product_option_info", "price", "sum_price"]

        extra_kwargs = {
            "user": {"write_only": True},
        }

    #TODO 동일한 옵션이 장바구니에 들어올 경우 count+
    # def create():
