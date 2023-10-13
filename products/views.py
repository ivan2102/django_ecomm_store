from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from products.models import Product
from django.db.models import Q

# Create your views here.
def products(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    else:

     products = Product.objects.all().filter(is_available=True).order_by('id')
     paginator = Paginator(products, 6)
     page = request.GET.get('page')
     paged_products = paginator.get_page(page) 
     product_count = products.count()

    context = {

        'products': paged_products,
        'product_count': product_count
    }
    return render(request, 'products/products.html', context)


def product_details(request, category_slug, product_slug):

    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    product_exists_in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    

    context = {

        'single_product': single_product,
         'product_exists_in_cart': product_exists_in_cart
    }
    return render(request, 'products/product_details.html', context)


def search(request):
   if 'keyword' in request.GET:
      keyword = request.GET['keyword']
      if keyword:
         products = Product.objects.order_by('-created_at').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
         product_count = products.count()

         context = {

            'products': products,
            'product_count': product_count
         }
   return render(request, 'products/products.html', context)
