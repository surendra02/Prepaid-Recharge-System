from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import Plan
from .serializers import PlanSerializer, UserSignupSerializer, UserLoginSerializer, RechargeSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(["POST"])
def signupUser(request):
    """It is use for signup with name,email,mobile and password"""
    if request.method == "POST":
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            user.set_password(serializer.data["password"])
            user.save()
            return Response({"success": "Account has been created!"})
        else:
            return Response(serializer.errors)


@api_view(["POST"])
def userLogin(request):
    """It is you for login with email and password which return a token"""
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        else:
            return Response({"error": "Invalid user credientials!"})


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def showPlan(request):
    """This function is use for show the plan if you have a valid token"""
    plan_data = Plan.objects.all()
    serializer = PlanSerializer(plan_data, many=True)
    return Response(serializer.data)


class RechargeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """It is use for Recharge as your given mobile number if you have a valid token"""
        serializer = RechargeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success":"Recharge successfully","data":serializer.data})
        else:
            return Response("Somthing went wrong!")