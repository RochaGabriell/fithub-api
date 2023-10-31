from django.db import models
from django.utils.translation import gettext_lazy as _

weekdays = [
    (1, _('Segunda-feira')),
    (2, _('Terça-feira')),
    (3, _('Quarta-feira')),
    (4, _('Quinta-feira')),
    (5, _('Sexta-feira')),
    (6, _('Sábado')),
    (7, _('Domingo')),
]


class WorkoutDay(models.Model):

    workout = models.ForeignKey(
        'Workout',
        verbose_name=_('Treino'),
        related_name='workoutdays',
        on_delete=models.CASCADE,
    )
    day = models.IntegerField(
        verbose_name=_('Dia da semana'),
        choices=weekdays,
    )
    description = models.TextField(
        verbose_name=_('Descrição do treino'),
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
        return f"{self.workout} - {weekdays[self.day - 1][1]}"

    class Meta:
        verbose_name = _('Treino do dia')
        verbose_name_plural = _('Treinos do dia')
        ordering = ['day']
