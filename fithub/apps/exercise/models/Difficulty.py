from django.db import models
from django.utils.translation import gettext_lazy as _


class Difficulty(models.Model):

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Dificuldade"),
        error_messages={
            "blank": _("Este campo não pode ficar em branco."),
            "null": _("Este campo não pode ser nulo."),
            "unique": _("Já existe uma dificuldade com este nome."),
        },
        max_length=45,
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Dificuldade")
        verbose_name_plural = _("Dificuldades")
        ordering = ["name"]
