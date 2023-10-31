from django.db import models
from django.utils.translation import gettext_lazy as _


class weekdays(models.Model):

    name = models.CharField(
        verbose_name=_('Nome do dia da semana'),
        max_length=40,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Dia da semana')
        verbose_name_plural = _('Dias da semana')
        ordering = ['name']
