from django.contrib import admin
from .models import User,Profile,Author,Book,Tag,BlogPost
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(BlogPost)