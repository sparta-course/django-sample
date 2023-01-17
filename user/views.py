from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.serializers import UserSerializer, UserCartSerializer

from user.models import User as UserModel
from user.models import Celler as CellerModel
from user.models import Cart as CartModel
from user.models import PurchaseList as PurchaseListModel
from user.models import PurchaseHistory as PurchaseHistoryModel


class UserView(APIView):
    # TODO 사용자 정보 조회
    def get(self, request):
        return Response({"message": "get method!!"})

    # DONE 회원가입
    # TODO 일반 사용자 가입 / 판매자 가입 나눠야 함
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    # TODO 회원 정보 수정
    def put(self, request):
        return Response({"message": "put method!!"})

    # TODO 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})


class UserAPIView(APIView):
    # DONE 로그인
    def post(self, request):
        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 비밀번호가 일치하지 않습니다."},
                            status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        return Response({"message": "login success!!"})

    # DONE 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"})


class UserCartView(APIView):
    # 사용자 장바구니 조회
    def get(self, request):
        carts = CartModel.objects.filter(user=request.user)
        return Response(UserCartSerializer(carts, many=True).data, status=status.HTTP_200_OK)

    # 장바구니 추가
    def post(self, request):
        request.data["user"] = request.user.id

        user_cart_serializer = UserCartSerializer(data=request.data)
        user_cart_serializer.is_valid(raise_exception=True)
        user_cart_serializer.save()

        return Response(user_cart_serializer.data, status=status.HTTP_200_OK)
