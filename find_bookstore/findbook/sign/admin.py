from django.contrib import admin
from sign.models import User, Tag, UserTag

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(UserTag)
