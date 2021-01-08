from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(req, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(req, 'shop/products/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(req, _id, product_slug):
    product = get_object_or_404(Product, id=_id, slug=product_slug, available=True)
    return render(req, 'shop/products/detail.html', {
        'product': product
    })
