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


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type_exercise',
        'difficulty',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'type_exercise',
        'difficulty',
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'is_main',
        'sex',
        'image',
    )
    search_fields = (
        'description',
    )
    list_filter = (
        'is_main',
    )
    ordering = (
        'id',
    )


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_front',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_front',
    )
    ordering = (
        'name',
    )


admin.site.register(Difficulty)
admin.site.register(Equipment)
admin.site.register(TypeExercise)
admin.site.register(WeightUnit)
