
# Register your models here.
from .models import Post, Category, Comment
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin




class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin): 
    summernote_fields = '__all__'
    list_display = ['title', 'author', 'category', 'created']
    search_fields = ['title', 'author', 'content']
    #list_filter = ('catgory', 'tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)