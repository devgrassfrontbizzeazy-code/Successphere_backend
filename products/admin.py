from django.contrib import admin
from django import forms
from django.db import models
from django.utils.html import format_html

from .models import Category, Product


# ======================================================
# Admin Site Branding
# ======================================================

admin.site.site_header = "Successphere Admin Portal"
admin.site.site_title = "Successphere Admin"
admin.site.index_title = "Welcome to Successphere Dashboard"


# ======================================================
# Category Admin
# ======================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


# ======================================================
# Product Admin
# ======================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # ---------- Product Thumbnail ----------
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                """
                <a href="{0}" target="_blank">
                    <img src="{0}"
                         style="
                            width:80px;
                            height:80px;
                            object-fit:cover;
                            border-radius:8px;
                            border:1px solid #ddd;
                        ">
                </a>
                """,
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Image"

    # ---------- List Page ----------
    list_display = (
        "image_preview",
        "id",
        "name",
        "category",
        "product_type",
        "moq_label",
        "moq_value",
        "created_at",
    )

    list_display_links = (
        "name",
    )

    search_fields = (
        "name",
        "description",
        "category__name",
        "product_type",
        "packaging",
    )

    list_filter = (
        "category",
        "product_type",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20

    date_hierarchy = "created_at"

    # ---------- Edit Page ----------
    readonly_fields = (
        "image_preview",
        "created_at",
        "updated_at",
    )

    fields = (
        "name",
        "category",
        "description",
        "product_type",
        "packaging",
        "moq_label",
        "moq_value",
        "image",
        "image_preview",
        "created_at",
        "updated_at",
    )

    # Better textarea size
    formfield_overrides = {
        models.TextField: {
            "widget": forms.Textarea(
                attrs={
                    "rows": 5,
                }
            )
        }
    }