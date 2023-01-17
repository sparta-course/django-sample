from django.db import models

class Product(models.Model):
    user = models.ForeignKey("user.User", verbose_name="사용자", on_delete=models.CASCADE)
    # thumbnail = models.FileField("", upload_to="product/thumnail/")
    # detail = models.FileField("", upload_to="product/detail/")
    title = models.CharField("제목", max_length=50)
    description = models.TextField("상품 설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)

    def __str__(self):
        return f"({self.id}){self.title} / {self.user.username} 님이 등록하신 상품입니다."

class ProductOption(models.Model):
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    name = models.CharField("옵션 명", max_length=50)
    price = models.IntegerField("가격")
    
    def __str__(self):
        return f"{self.product}의 옵션입니다. / {self.name}, {self.price}원"
    

class Review(models.Model):
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", verbose_name="사용자", on_delete=models.CASCADE)
    rating = models.IntegerField("평점")
    content = models.TextField("내용")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    
    def __str__(self):
        return f"{self.product}에 달린 {self.user.username}님의 리뷰입니다. / {self.content}"