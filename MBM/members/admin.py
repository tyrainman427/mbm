from django.contrib import admin
from .models import Member, Tweet, Follow

# Register your models here.
admin.site.register(Member)
admin.site.register(Tweet)
admin.site.register(Follow)
