from django.contrib import admin
from .models import Post,UserProfile,Business,Neighbourhood


# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Neighbourhood)

