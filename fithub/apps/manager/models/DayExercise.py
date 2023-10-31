from django.db import models
from django.utils.translation import gettext_lazy as _

from fithub.apps.exercise.models import Exercise


class DayExercise(models.Model):

    day_list = models.ForeignKey(
        'WorkoutDay',
        verbose_name=_('Lista de dias'),
        related_name='dayexercises',
        on_delete=models.CASCADE,
    )
    exercise = models.ForeignKey(
        Exercise,
        verbose_name=_('Exercício'),
        related_name='dayexercises',
        on_delete=models.CASCADE,
    )
    repetitions = models.IntegerField(
        verbose_name=_('Repetições'),
        blank=True,
        null=True,
    )
    weight = models.IntegerField(
        verbose_name=_('Peso'),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Data de criação'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Data de atualização'),
        auto_now=True,
    )

    def __str__(self):
        return self.exercise.name

    class Meta:
        verbose_name = _('Exercício do dia')
        verbose_name_plural = _('Exercícios do dia')
        ordering = ['day_list', 'exercise']
