from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from almost_rozetka.models import CustomUser, City, Company, Product
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Purchases'), {
            'fields': ('product', 'city')})
    )
