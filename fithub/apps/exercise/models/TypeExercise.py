from django.db import models
from django.utils.translation import gettext_lazy as _

# (1, _("Cardio")),
# (3, _("Força")),
# (4, _("Alongamento")),
# (6, _("Calistenia")),
# (7, _("Crossfit")),


class TypeExercise(models.Model):

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Nome do tipo de exercício"),
        max_length=45,
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Tipo de exercício")
        verbose_name_plural = _("Tipos de exercícios")
        ordering = ["name"]
