from django.db import models
from django.utils.translation import gettext_lazy as _


class DayList(models.Model):

    workout = models.ForeignKey(
        'Workout',
        verbose_name=_('Treino'),
        related_name='daylists',
        on_delete=models.CASCADE,
    )
    day = models.ForeignKey(
        'Weekdays',
        verbose_name=_('Dia da semana'),
        related_name='daylists',
        on_delete=models.CASCADE,
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
        return self.day.name

    class Meta:
        verbose_name = _('Dia da semana')
        verbose_name_plural = _('Dias da semana')
        ordering = ['day']
