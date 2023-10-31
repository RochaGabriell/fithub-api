from django.contrib import admin

# Register your models here.

from .models import (
    Exercise,
    Image,
    Difficulty,
    Equipment,
    Muscle,
    TypeExercise,
    WeightUnit,
)

admin.site.register(Exercise)
admin.site.register(Image)
admin.site.register(Difficulty)
admin.site.register(Equipment)
admin.site.register(Muscle)
admin.site.register(TypeExercise)
admin.site.register(WeightUnit)
