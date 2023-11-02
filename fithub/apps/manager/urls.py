from rest_framework.routers import DefaultRouter

from fithub.apps.manager.views import (
    DayExerciseViewSet,
    WorkoutDayViewSet,
    WorkoutViewSet,
)

router = DefaultRouter()

router.register(r"day_exercise", DayExerciseViewSet)
router.register(r"workout_day", WorkoutDayViewSet)
router.register(r"workout", WorkoutViewSet)

urlpatterns = router.urls
