from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Nombre del producto
    description = models.TextField()  # Descripción del producto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    image = models.ImageField(upload_to='products/')  # Imagen del producto
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.name
