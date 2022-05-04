from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    mobile = models.CharField(max_length=10, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name", "mobile"]
    objects = UserManager()


class Operator(models.Model):
    operator_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.operator_name


class AreaCircle(models.Model):
    area = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.area


class CategoryPlan(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Plan(models.Model):
    DATATYPE_CHOICES = (("MB", "MB"), ("GB", "GB"), ("MB/Day", "MB/Day"), ("GB/Day", "GB/Day"))
    plan_type = models.ForeignKey(CategoryPlan, on_delete=models.CASCADE, related_name="type")
    price = models.PositiveIntegerField(unique=True)
    validity = models.PositiveIntegerField()
    data = models.FloatField(max_length=5)
    data_type = models.CharField(choices=DATATYPE_CHOICES, max_length=30)
    description = models.TextField(max_length=250)

    def __str__(self):
        return str(self.price) + " " + str(self.data) + "" + self.data_type


class Recharge(models.Model):
    mobile = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="email")
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, to_field="operator_name")
    circle = models.ForeignKey(AreaCircle, on_delete=models.CASCADE, to_field="area")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, to_field="price", related_name="plan_detail")
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "Mobile no : " + str(self.mobile) + " plan : " + str(self.plan) + " Operator : " + str(
            self.operator) + " by :" + str(self.user)
