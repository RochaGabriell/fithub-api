from django.db import models
from django.utils.translation import gettext_lazy as _


class Muscle(models.Model):

    name = models.CharField(
        _('Nome'),
        help_text=_('Nome do músculo'),
        max_length=45,
        blank=False,
        null=False,
        unique=True,
    )
    is_front = models.BooleanField(
        _("Musculo frontal"),
        help_text=_("Musculo frontal"),
        default=True,
        blank=False,
        null=False,
    )
