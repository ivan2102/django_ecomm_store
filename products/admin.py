from django.contrib import admin
from .models import Product, Variation

class AdminProduct(admin.ModelAdmin):
   list_display = ('product_name', 'price', 'stock', 'category', 'is_available', 'modified_at')
   prepopulated_fields = {'slug': ('product_name', )}

class VariationAdmin(admin.ModelAdmin):
   list_display = ('product', 'variation_category', 'variation_value', 'is_active')
   list_editable = ('is_active', )
   list_filter = ('product', 'variation_category', 'variation_value')


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Variation, VariationAdmin)
