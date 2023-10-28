from django.contrib import admin

# Register your models here.

from .models import Exercise
from .models import Image
from .models import Difficulty
from .models import Equipment
from .models import Muscle
from .models import TypeExercise
from .models import WeightUnit

admin.site.register(Exercise)
admin.site.register(Image)
admin.site.register(Difficulty)
admin.site.register(Equipment)
admin.site.register(Muscle)
admin.site.register(TypeExercise)
admin.site.register(WeightUnit)
