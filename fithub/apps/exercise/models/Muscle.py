from django.db import models
from django.utils.translation import gettext_lazy as _


class Muscle(models.Model):

    name = models.CharField(
        verbose_name=_('Nome'),
        help_text=_('Nome do músculo'),
        error_messages={
            "blank": _("Este campo não pode ficar em branco."),
            "null": _("Este campo não pode ser nulo."),
            "unique": _("Já existe um músculo com este nome."),
        },
        max_length=45,
        unique=True,
    )
    is_front = models.BooleanField(
        verbose_name=_("Musculo frontal"),
        default=True,
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = _('Musculo')
        verbose_name_plural = _('Musculos')
        ordering = ['name']
