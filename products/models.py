from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre de la categoría
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    class Meta:
        verbose_name_plural = "Categories"  # Nombre plural en el admin

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Relación con categoría
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name