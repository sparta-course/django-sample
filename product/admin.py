from django.contrib import admin

from product.models import Product as ProductModel
from product.models import ProductOption as ProductOptionModel
from product.models import Review as ReviewModel

admin.site.register(ProductModel)
admin.site.register(ProductOptionModel)
admin.site.register(ReviewModel)