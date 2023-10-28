from django.db import models
from django.utils.translation import gettext_lazy as _


class Equipment(models.Model):

    name = models.CharField(
        verbose_name=_('Nome do equipamento'),
        max_length=45,
        unique=True
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = _('Equipamento')
        verbose_name_plural = _('Equipamentos')
        ordering = ['name']
