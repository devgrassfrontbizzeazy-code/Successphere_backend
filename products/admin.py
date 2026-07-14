from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "product_type",
        "moq_label",
        "created_at",
    )

    search_fields = (
        "name",
        "category__name",
        "product_type",
    )

    list_filter = (
        "category",
        "product_type",
    )