from django.db import models
from django.utils.translation import gettext_lazy as _


class Equipment(models.Model):

    name = models.CharField(
        verbose_name=_('Nome do equipamento'),
        max_length=45,
        blank=False,
        null=False,
        unique=True
    )
