from rest_framework import serializers
from .models import Plan, CategoryPlan, User, Recharge
import phonenumbers
from phonenumbers import carrier


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "name", "mobile"]

    def validate(self, attrs):
        mobile=attrs.get("mobile")
        name=attrs.get("name")
        if str(mobile).isdigit() and len(mobile)==10:
            if str(name).isalpha():
                return attrs
            else:
                raise serializers.ValidationError("Enter a valid name")
        else:
            raise serializers.ValidationError("Enter a valid mobile number")

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "password"]


class CategoryPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPlan
        fields = ["category_name"]


class PlanSerializer(serializers.ModelSerializer):
    plan_type = serializers.SerializerMethodField("get_plan")

    class Meta:
        model = Plan
        fields = ["price", "validity", "data", "data_type", "description", "plan_type"]

    def get_plan(self, obj):
        category = CategoryPlan.objects.get(id=obj.plan_type.id)
        serializer = CategoryPlanSerializer(category)
        return serializer.data


############ Resposible for Recharge #################

class RechargeSerializer(serializers.ModelSerializer):
    plan_details = serializers.SerializerMethodField("get_plan_detail")

    class Meta:
        model = Recharge
        fields = ["mobile", "user", "operator", "circle", "plan","date","plan_details"]

    def get_plan_detail(self, obj):
        data = Plan.objects.filter(price=obj.plan.price)
        serializer = PlanSerializer(data, many=True)
        return serializer.data

    def validate(self, attrs):
        mobile = attrs.get("mobile")
        operator = attrs.get("operator")
        if len(mobile) < 10 or len(mobile) > 10:
            raise serializers.ValidationError("Invailed mobile number, Please enter your 10 digit of mobile number")
        mobile = "+91" + mobile
        phoneNumber = phonenumbers.parse(mobile)
        print(phoneNumber)
        Carrier = carrier.name_for_number(phoneNumber, 'en')

        if str(Carrier) != str(operator):
            raise serializers.ValidationError("Please enter the valid operator!")
        return attrs
