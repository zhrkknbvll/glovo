from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Store, Product, Userprofile, Order, Courier, Review

class CategoryAdmin(TranslationAdmin):
    list_display = ('category_name',)

class StoreAdmin(TranslationAdmin):
    list_display = ('store_name',)

class ProductAdmin(TranslationAdmin):
    list_display = ('product_name', 'price')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Userprofile)
admin.site.register(Order)
admin.site.register(Courier)
admin.site.register(Review)