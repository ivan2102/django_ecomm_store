from django.contrib import admin
from .models import Product, ProductImageGallery, Variation, ReviewRating
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductImageGalleryInline(admin.TabularInline):
   model = ProductImageGallery
   extra = 1

class AdminProduct(admin.ModelAdmin):
   list_display = ('product_name', 'price', 'stock', 'category', 'is_available', 'modified_at')
   prepopulated_fields = {'slug': ('product_name', )}
   inlines = [ProductImageGalleryInline]

class VariationAdmin(admin.ModelAdmin):
   list_display = ('product', 'variation_category', 'variation_value', 'is_active')
   list_editable = ('is_active', )
   list_filter = ('product', 'variation_category', 'variation_value')


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductImageGallery)
