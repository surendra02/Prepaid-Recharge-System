from . import views
from django.urls import path

urlpatterns = [
    path("user-signup/",views.signupUser),
    path("user-signin/",views.userLogin),
    path("plans/",views.showPlan),
    path('recharge/',views.RechargeView.as_view()),
]
