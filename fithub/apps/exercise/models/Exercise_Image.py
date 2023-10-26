from django.db import models
from django.utils.translation import gettext_lazy as _

from fithub.apps.exercise.models.Exercise import Exercise


class Exercise_Image(models.Model):

    exercise = models.ForeignKey(
        Exercise,
        verbose_name=_("Exercício"),
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text=_("Exercício"),
    )
    image = models.ImageField(
        _("Imagem"),
        upload_to="exercise_images",
        blank=False,
        null=False,
        help_text=_("Imagem do exercício"),
    )
    is_main = models.BooleanField(
        _("Imagem principal"),
        default=True,
        blank=False,
        null=False,
        help_text=_("Imagem principal do exercício"),
    )
    description = models.CharField(
        _("Descrição"),
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Descrição da imagem"),
    )

    def __str__(self) -> str:
        return f"{self.exercise.name} - {self.description}"

    class Meta:
        verbose_name = _("Imagem do exercício")
        verbose_name_plural = _("Imagens dos exercícios")
