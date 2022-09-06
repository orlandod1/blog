from django.contrib import admin
from post.models import CategoryPost,Post
# Register your models here.

admin.site.register(Post)
admin.site.register(CategoryPost)