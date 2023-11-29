from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):

    exercise = models.ForeignKey(
        "Exercise",
        verbose_name=_("Exercício"),
        related_name="images",
        help_text=_("Exercício ao qual a imagem pertence"),
        on_delete=models.PROTECT,
    )
    image = models.ImageField(
        verbose_name=_("Imagem"),
        help_text=_("Apenas PNG, JPG, SVG e GIF"),
        upload_to="media/exercise_images/",
    )
    is_main = models.BooleanField(
        verbose_name=_("Imagem principal"),
        help_text=_("Marque a caixa se quiser definir esta imagem como principal para o exercício (será mostrada, por exemplo, na pesquisa). A primeira imagem é marcada automaticamente pelo sistema."),
        default=True,
    )
    sex = models.CharField(
        verbose_name=_("Sexo"),
        help_text=_("Sexo para o qual a imagem é destinada"),
        max_length=1,
        choices=(
            ("M", _("Masculino")),
            ("F", _("Feminino"))
        ),
        default="M",
    )
    description = models.CharField(
        verbose_name=_("Descrição"),
        help_text=_("Nome da imagem"),
        max_length=45,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.exercise.name}"

    class Meta:
        verbose_name = _("Imagem do exercício")
        verbose_name_plural = _("Imagens dos exercícios")
        ordering = ["-is_main", "description"]
