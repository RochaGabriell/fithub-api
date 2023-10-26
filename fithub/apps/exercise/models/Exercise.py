from django.db import models
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):

    TYPE_EXERCISE = (
        (1, _("Cardio")),
        (2, "Powerlifting"),
        (3, "Strength"),
        (4, _("Alongamento")),
        (5, "Strongman"),
    )
    DIFFICULTY = (
        (1, _("Iniciante")),
        (2, _("Intermediário")),
        (3, _("Avançado")),
    )
    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Nome do exercício"),
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    type_exercise = models.IntegerField(
        verbose_name=_("Tipo de exercício"),
        help_text=_("Tipo de exercício"),
        choices=TYPE_EXERCISE,
        blank=False,
        null=False,
    )
    difficulty = models.IntegerField(
        verbose_name=_("Dificuldade"),
        help_text=_("Dificuldade do exercício"),
        choices=DIFFICULTY,
        blank=False,
        null=False,
    )
    instructions = models.TextField(
        verbose_name=_("Instruções"),
        help_text=_("Instruções do exercício"),
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Exercício")
        verbose_name_plural = _("Exercícios")
