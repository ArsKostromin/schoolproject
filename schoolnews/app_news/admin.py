from .models import Product, Rubric, Comment 
from django.contrib import admin



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)

class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ('rubric')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('product','created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('body',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rubric)


