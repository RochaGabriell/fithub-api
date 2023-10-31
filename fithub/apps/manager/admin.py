from django.contrib import admin

from .models import (
    DayExercise,
    Workout,
    WorkoutDay,
)

admin.site.register(DayExercise)
admin.site.register(Workout)
admin.site.register(WorkoutDay)
