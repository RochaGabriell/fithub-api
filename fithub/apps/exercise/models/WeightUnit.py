from django.db import models
from django.utils.translation import gettext_lazy as _


class WeightUnit(models.Model):

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Unidade do exercício"),
        max_length=45,
        unique=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Unidade de peso")
        verbose_name_plural = _("Unidades de peso")
        ordering = ["name"]
