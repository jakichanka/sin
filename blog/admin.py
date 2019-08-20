from django.contrib import admin
from blog.models import *
# Register your models here.

admin.site.register(About)
class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
