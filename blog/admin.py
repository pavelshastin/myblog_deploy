from django.contrib import admin
from .models import Post, Comment, MyUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)


# admin.site.register(Author)
# admin.site.register(Blog)
# admin.site.register(Entry)

# Register your models here.
