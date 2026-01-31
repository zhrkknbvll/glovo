from modeltranslation.translator import register, TranslationOptions
from .models import Category, Store, Product

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'product_description')