from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from orders.models import ProductOrder
from products.forms import ReviewRatingForm
from products.models import Product, ProductImageGallery, ReviewRating, Variation
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

    if request.user.is_authenticated:

      try:
       product_order = ProductOrder.objects.filter(user=request.user, product_id=single_product.id).exists()

      except ProductOrder.DoesNotExist:
       product_order = None

      else:
         product_order = None


    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)   
    product_gallery = ProductImageGallery.objects.filter(product_id=single_product.id)  
    

    context = {

        'single_product': single_product,
         'product_exists_in_cart': product_exists_in_cart,
         'product_order': product_order,
         'reviews': reviews,
         'product_gallery': product_gallery
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

def reviews(request, product_id):
   url = request.META.get('HTTP_REFERER')
   if request.method == 'POST':
      
      try:
         reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
         form = ReviewRatingForm(request.POST, instance=reviews)
         form.save()
         messages.success(request, 'Thank you! Your review has been updated successfully')
         return redirect(url)
      
      except ReviewRating.DoesNotExist:
         form = ReviewRatingForm(request.POST)
         if form.is_valid():
            data = ReviewRating()
            data.subject = form.cleaned_data['subject']
            data.review = form.cleaned_data['review']
            data.rating = form.cleaned_data['rating']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = product_id
            data.user_id = request.user.id
            data.save()
            messages.success(request, 'Thank you! Your review successfully recorded')
            return redirect(url)
