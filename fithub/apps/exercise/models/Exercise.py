from django.db import models
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Nome do exercício"),
        error_messages={
            "blank": _("Este campo não pode ficar em branco."),
            "null": _("Este campo não pode ser nulo."),
            "unique": _("Já existe um exercício com este nome."),
        },
        max_length=255,
        unique=True,
    )
    type_exercise = models.ForeignKey(
        "TypeExercise",
        verbose_name=_("Tipo de exercício"),
        related_name="exercises",
        help_text=_("Tipo de exercício"),
        on_delete=models.PROTECT,
    )
    difficulty = models.ForeignKey(
        "Difficulty",
        verbose_name=_("Dificuldade"),
        related_name="exercises",
        help_text=_("Dificuldade do exercício"),
        on_delete=models.PROTECT,
    )
    instructions = models.TextField(
        verbose_name=_("Instruções"),
        help_text=_("Instruções do exercício"),
        error_messages={
            "blank": _("Este campo não pode ficar em branco."),
            "null": _("Este campo não pode ser nulo."),
        },
    )
    muscles_primary = models.ManyToManyField(
        "Muscle",
        verbose_name=_("Músculo primário"),
        related_name="muscles_primary_exercises",
        help_text=_("Músculo primário utilizado"),
    )
    muscles_secondary = models.ManyToManyField(
        "Muscle",
        verbose_name=_("Músculo secundário"),
        related_name="muscles_secondary_exercises",
        help_text=_("Músculo secundário utilizado"),
        blank=True,
    )
    equipment = models.ManyToManyField(
        "Equipment",
        verbose_name=_("Equipamento"),
        related_name="exercises",
        help_text=_("Equipamento utilizado"),
        blank=True,
    )
    variations = models.ManyToManyField(
        "self",
        verbose_name=_("Variações"),
        help_text=_("Variações do exercício"),
        blank=True,
        symmetrical=True,  # Permite que a relação seja simétrica, ou seja, se A está relacionado com B, B também está relacionado com A
    )
    weight_unit = models.ForeignKey(
        "WeightUnit",
        verbose_name=_("Unidade de peso"),
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Exercício")
        verbose_name_plural = _("Exercícios")
        ordering = ["name"]
