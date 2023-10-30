from django.db import models
from django.utils.translation import ugettext_lazy as _


class Measurements(models.Model):

    user = models.ForeignKey(
        "User",
        verbose_name=_("Usuário"),
        related_name="measurements",
        on_delete=models.CASCADE,
    )
    weight = models.DecimalField(
        verbose_name=_("Peso"),
        max_digits=5,
        decimal_places=2,
    )
    height = models.DecimalField(
        verbose_name=_("Altura"),
        max_digits=3,
        decimal_places=2,
    )
    chest = models.DecimalField(
        verbose_name=_("Peito"),
        max_digits=3,
        decimal_places=2,
    )
    waist = models.DecimalField(
        verbose_name=_("Cintura"),
        max_digits=3,
        decimal_places=2,
    )
    abdomen = models.DecimalField(
        verbose_name=_("Abdômen"),
        max_digits=3,
        decimal_places=2,
    )
    hip = models.DecimalField(
        verbose_name=_("Quadril"),
        max_digits=3,
        decimal_places=2,
    )
    right_forearm = models.DecimalField(
        verbose_name=_("Antebraço direito"),
        max_digits=3,
        decimal_places=2,
    )
    left_forearm = models.DecimalField(
        verbose_name=_("Antebraço esquerdo"),
        max_digits=3,
        decimal_places=2,
    )
    right_arm = models.DecimalField(
        verbose_name=_("Braço direito"),
        max_digits=3,
        decimal_places=2,
    )
    left_arm = models.DecimalField(
        verbose_name=_("Braço esquerdo"),
        max_digits=3,
        decimal_places=2,
    )
    right_thigh = models.DecimalField(
        verbose_name=_("Coxa direita"),
        max_digits=3,
        decimal_places=2,
    )
    left_thigh = models.DecimalField(
        verbose_name=_("Coxa esquerda"),
        max_digits=3,
        decimal_places=2,
    )
    right_calf = models.DecimalField(
        verbose_name=_("Panturrilha direita"),
        max_digits=3,
        decimal_places=2,
    )
    left_calf = models.DecimalField(
        verbose_name=_("Panturrilha esquerda"),
        max_digits=3,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Criado em"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Atualizado em"),
        auto_now=True,
    )

    def __str__(self):
        return f"{self.user} - {self.created_at}"

    class Meta:
        verbose_name = _("Medida")
        verbose_name_plural = _("Medidas")
        ordering = ["-created_at"]
