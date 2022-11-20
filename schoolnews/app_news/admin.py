from .models import Product, Rubric 
from django.contrib import admin



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)

class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ('rubric')



admin.site.register(Product, ProductAdmin)
admin.site.register(Rubric)