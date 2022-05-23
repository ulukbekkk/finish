from django.contrib import admin

from .models import Category, Product, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'category', 'created_at',)
    list_display_links = ('title', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',  )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)