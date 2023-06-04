from django.contrib import admin

# Register your models here.

#from .models import Post
from .models import *
admin.site.register(Exclusive)
admin.site.register(Best)
admin.site.register(LatestBlog)
#admin.site.register(Post)