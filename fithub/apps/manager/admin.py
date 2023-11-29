from django.contrib import admin

from .models import (
    DayExercise,
    Workout,
    WorkoutDay,
)


@admin.register(WorkoutDay)
class WorkoutDayAdmin(admin.ModelAdmin):
    list_display = ('workout', 'day', 'created_at')


@admin.register(DayExercise)
class DayExerciseAdmin(admin.ModelAdmin):
    list_display = ('day_list', 'exercise', 'series',
                    'repetitions', 'weight', 'created_at')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'difficulty', 'public', 'created_at')
