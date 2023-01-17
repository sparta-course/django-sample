from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50, unique=True)
    email = models.EmailField("이메일", unique=True)
    password = models.CharField("비밀번호", max_length=150)
    fullname = models.CharField("이름", max_length=30)
    phone = models.CharField("핸드폰번호", max_length=20)

    is_active = models.BooleanField("계정 활성화 여부", default=True)
    is_admin = models.BooleanField("admin 권한", default=False)

    cart = models.ManyToManyField("product.ProductOption", verbose_name="장바구니", through='Cart', related_name="carts")
    like = models.ManyToManyField("product.Product", verbose_name="좋아요 한 상품", related_name="likes")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

class Celler(models.Model):
    user = models.OneToOneField(User, verbose_name="사용자", on_delete=models.CASCADE)
    approval_date = models.DateTimeField("승인 일자", null=True) # 해당 값이 null일 경우 아직 승인되지 않음

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="사용자", on_delete=models.CASCADE, related_name="users")
    product_option = models.ForeignKey("product.ProductOption", verbose_name="상품", on_delete=models.CASCADE)
    count = models.IntegerField("수량")

class PurchaseList(models.Model):
    STATUS = (
        ("ready", "배송 준비중"),
        ("delivery", "배송중"),
        ("done", "배송 완료"),
    )

    user = models.ForeignKey(User, verbose_name="사용자", on_delete=models.CASCADE)
    # product
    count = models.IntegerField("수량")
    status = models.CharField("배송 상태",choices=STATUS ,max_length=10)

class PurchaseHistory(models.Model):
    PAYMENT_TYPE = (
        ("card", "카드"),
        ("cash", "무통장 입금"),
    )

    purchase_list = models.ManyToManyField(PurchaseList, verbose_name="구매 목록")
    payment_type = models.CharField("결제 방식",choices=PAYMENT_TYPE ,max_length=50)
    payment_datetime = models.DateTimeField("결제일시", auto_now_add=True)
