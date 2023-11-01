from rest_framework.routers import DefaultRouter
from fithub.apps.exercise.views import (
    DifficultyViewSet,
    EquipmentViewSet,
    ExerciseViewSet,
    ImageViewSet,
    MuscleViewSet,
    TypeExerciseViewSet,
    WeightUnitViewSet,
)

app_name = "exercise"

router = DefaultRouter(trailing_slash=False)

router.register(r"difficulty", DifficultyViewSet, basename="difficulty")
router.register(r"equipment", EquipmentViewSet, basename="equipment")
router.register(r"exercise", ExerciseViewSet, basename="exercise")
router.register(f"image", ImageViewSet, basename="image")
router.register(r"muscle", MuscleViewSet, basename="muscle")
router.register(r"type-exercise", TypeExerciseViewSet, basename="type-exercise")
router.register(r"weight-unit", WeightUnitViewSet, basename="weight-unit")

urlpatterns = router.urls
