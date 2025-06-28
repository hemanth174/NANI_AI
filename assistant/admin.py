from django.contrib import admin
from .models import Command, UserQuery, Response

admin.site.register(Command)
admin.site.register(UserQuery)
admin.site.register(Response)