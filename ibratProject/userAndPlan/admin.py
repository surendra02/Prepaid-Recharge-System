from django.contrib import admin
from .models import User, AreaCircle, Operator,CategoryPlan,Plan,Recharge


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "mobile", "password"]


admin.site.register(AreaCircle)
admin.site.register(Operator)
admin.site.register(CategoryPlan)
admin.site.register(Plan)
admin.site.register(Recharge)


