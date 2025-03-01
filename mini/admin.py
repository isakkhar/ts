from django.contrib import admin

from mini.models import Author, Category, Post


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['Author_Name', 'Email']
    list_filter = ['Author_Name', 'Email']
    search_fields = ['Author_Name', 'Email']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name']
    search_fields = ['Name']
    list_filter = ['Name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Author_Name', 'Category']
    search_fields = ['Title', 'Author_Name', 'Category']
    list_filter = ['Title', 'Author_Name', 'Category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


    # class PostAdmin(admin.ModelAdmin):
    #     list_display = ('Title')
admin.site.register(Author, AuthorAdmin)
# @admin.register(Post)

