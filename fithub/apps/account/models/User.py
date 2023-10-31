from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from fithub.apps.account.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=40,
    )
    username = models.CharField(
        verbose_name=_("Nome de usuário"),
        error_messages={
            'unique': _("Já existe um usuário com este nome de usuário."),
        },
        max_length=40,
        unique=True,
    )
    email = models.EmailField(
        verbose_name=_("Endereço de e-mail"),
        error_messages={
            'unique': _("Já existe um usuário com este e-mail."),
        },
        max_length=254,
        unique=True,
    )
    birth_date = models.DateField(
        verbose_name=_("Data de nascimento"),
        null=True,
        blank=True,
    )
    sex = models.CharField(
        verbose_name=_("Sexo"),
        max_length=1,
        choices=(
            ("M", "Masculino"),
            ("F", "Feminino"),
        ),
        null=True,
        blank=True,
    )

    is_staff = models.BooleanField(
        verbose_name=_("Equipe"),
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Super Usuário"),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_("Ativo"),
        default=True,
    )
    
    date_joined = models.DateTimeField(
        verbose_name=_("data de entrada"),
        auto_now_add=True,
    )
    date_changed = models.DateTimeField(
        verbose_name=_("data de alteração"),
        auto_now=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)

    def show_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return f"{self.username} - {self.email}"

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
        ordering = ["-date_joined"]
