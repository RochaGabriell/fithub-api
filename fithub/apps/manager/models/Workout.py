from django.db import models
from django.utils.translation import gettext_lazy as _

from fithub.apps.account.models import User
from fithub.apps.exercise.models import Difficulty


class Workout(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name=_('Usuário'),
        related_name='workouts',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_('Nome do treino'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('Descrição do treino'),
    )
    difficulty = models.ForeignKey(
        Difficulty,
        verbose_name=_("Dificuldade"),
        related_name="workouts",
        help_text=_("Dificuldade do treino"),
        on_delete=models.PROTECT,
    )
    public = models.BooleanField(
        verbose_name=_('Público'),
        help_text=_(
            'Se marcado, este treino será visível para outros usuários'),
        default=True,
    )
    default = models.BooleanField(
        verbose_name=_('Padrão'),
        help_text=_(
            'Se marcado, este treino será o padrão para aparecer na página inicial'),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Data de criação'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Data de atualização'),
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Treino')
        verbose_name_plural = _('Treinos')
        ordering = ['name']
