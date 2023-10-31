from django.contrib import admin

from .models import (
    User,
    Measurements,
)

admin.site.register(User)
admin.site.register(Measurements)
