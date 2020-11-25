from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','modify_at')
    list_filter = ('modify_at',)
    search_fields = ("title",'content')
    prepopulated_fields = {'slug': ('title',)}