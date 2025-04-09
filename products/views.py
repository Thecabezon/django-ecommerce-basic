from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    category_id = request.GET.get('category')  # Obtener la categoría desde la URL
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('-created_at')
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        products = Product.objects.all().order_by('-created_at')
        selected_category = None

    categories = Category.objects.all()  # Obtener todas las categorías
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})