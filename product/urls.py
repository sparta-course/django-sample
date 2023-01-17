from django.urls import path, include

from product import views

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('detail/<product_id>/', views.ProductDetailView.as_view()),
    path('review/update/<review_id>/', views.ReviewView.as_view()),
    path('review/<product_id>/', views.ReviewView.as_view()),
    path('<int:product_id>/', views.ProductView.as_view()),
]
