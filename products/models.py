from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    description = models.TextField()

    moq_label = models.CharField(max_length=50)

    moq_value = models.IntegerField()

    packaging = models.CharField(max_length=255)

    product_type = models.CharField(max_length=150)

    image = models.ImageField(
        upload_to="products/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name