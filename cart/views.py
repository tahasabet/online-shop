from itertools import product

from django.shortcuts import render,get_object_or_404
from pyexpat.errors import messages
from django.contrib import messages
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()
    return render(request,'cart_summary.html',{'cart_products':cart_products,'quantities':quantities,'total':total})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()
        #response = JsonResponse({'Product name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, f'Successfully added {product.name} to cart')
        return response


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        # دریافت محصول از پایگاه داده
        product = get_object_or_404(Product, id=product_id)

        # حذف محصول از سبد خرید
        cart.delete(product=product_id)

        # پیام موفقیت
        messages.success(request, f'Successfully deleted {product.name}')

        # پاسخ JSON
        response = JsonResponse({'product': product_id})
        return response


def cart_update(request):
    cart = Cart(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        print(request.POST)  # بررسی داده‌های POST
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')


        if not product_id or not product_qty:
            return JsonResponse({'error': 'Missing product_id or product_qty'}, status=400)

        try:
            product_id = int(product_id)
            product_qty = int(product_qty)

            cart.update(product=product_id, quantity=product_qty)

            return JsonResponse({'qty': product_qty})

        except ValueError:
            return JsonResponse({'error': 'Invalid product_id or product_qty'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    return JsonResponse({'error': 'Invalid request'}, status=400)
