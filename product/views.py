from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from product import serializers

from product.serializers import ProductSerializer, ReviewSerializer, ProductDetailSerializer

from user.models import User as UserModel
from user.models import Celler as CellerModel
from user.models import Cart as CartModel
from user.models import PurchaseList as PurchaseListModel
from user.models import PurchaseHistory as PurchaseHistoryModel

from product.models import Product as ProductModel
from product.models import ProductOption as ProductOptionModel
from product.models import Review as ReviewModel

from rest_framework import viewsets

class ProductView(APIView):
    #DONE 상품 목록 조회
    def get(self, request):
        return Response(ProductSerializer(ProductModel.objects.all(), many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data["user"] = request.user.id

        product_serializer = ProductSerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()

        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "존재하지 않는 product입니다."},
                            status=status.HTTP_400_BAD_REQUEST)

        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()

        return Response(product_serializer.data, status=status.HTTP_200_OK)

    #TODO 상품 삭제
    def delete(self, request):
        return Response({"message": "delete method!!"})

class ProductDetailView(APIView):
    def get(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "존재하지 않는 product입니다."},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(ProductDetailSerializer(product).data, status=status.HTTP_200_OK)

class ReviewView(APIView):
    def post(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "존재하지 않는 product입니다."},
                            status=status.HTTP_400_BAD_REQUEST)

        data = request.data.dict()
        data["user"] = request.user.id
        data["product"] = product.id
        review_serializer = ReviewSerializer(data=data)
        review_serializer.is_valid(raise_exception=True)
        review_serializer.save()

        return Response(review_serializer.data, status=status.HTTP_200_OK)

    #TODO 리뷰 수정
    def put(self, request, review_id):
        return Response({})

    #TODO 리뷰 삭제
    def delete(self, request, review_id):
        return Response({})
