from django.db import models
from django.utils.translation import ugettext_lazy as _

my_measurement = {
    "weight/Peso": 76.5,
    "height/Altura": 180,

    "shoulder/Ombro": 112,
    "chest/Peito": 102.2,
    "right_arm/Braço direito": 31.2,
    "left_arm/Braço esquerdo": 31,
    "right_forearm/Antebraço direito": 28.6,
    "left_forearm/Antebraço esquerdo": 28.2,
    "right_fist/Punho direito": 18,
    "left_fist/Punho esquerdo": 18,

    "waist/Cintura": 75.5,
    "abdomen/Abdômen": 79.5,
    "hip/Quadril": 97.7,

    "right_thigh/Coxa direita": 53.8,
    "left_thigh/Coxa esquerda": 53.8,
    "right_calf/Panturrilha direita": 37.5,
    "left_calf/Panturrilha esquerda": 38,
}
# bmi = 76.5 / (1.8 * 1.8) = 23.61 (Peso normal)
# rcq = 75.5 / 97.7 = 0.77 (Baixo)


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
    shoulder = models.DecimalField(
        verbose_name=_("Ombro"),
        max_digits=4,
        decimal_places=2,
    )
    chest = models.DecimalField(
        verbose_name=_("Peito"),
        max_digits=4,
        decimal_places=2,
    )
    right_arm = models.DecimalField(
        verbose_name=_("Braço direito"),
        max_digits=4,
        decimal_places=2,
    )
    left_arm = models.DecimalField(
        verbose_name=_("Braço esquerdo"),
        max_digits=4,
        decimal_places=2,
    )
    right_forearm = models.DecimalField(
        verbose_name=_("Antebraço direito"),
        max_digits=4,
        decimal_places=2,
    )
    left_forearm = models.DecimalField(
        verbose_name=_("Antebraço esquerdo"),
        max_digits=4,
        decimal_places=2,
    )
    right_fist = models.DecimalField(
        verbose_name=_("Punho direito"),
        max_digits=4,
        decimal_places=2,
    )
    left_fist = models.DecimalField(
        verbose_name=_("Punho esquerdo"),
        max_digits=4,
        decimal_places=2,
    )
    waist = models.DecimalField(
        verbose_name=_("Cintura"),
        max_digits=4,
        decimal_places=2,
    )
    abdomen = models.DecimalField(
        verbose_name=_("Abdômen"),
        max_digits=4,
        decimal_places=2,
    )
    hip = models.DecimalField(
        verbose_name=_("Quadril"),
        max_digits=4,
        decimal_places=2,
    )
    right_thigh = models.DecimalField(
        verbose_name=_("Coxa direita"),
        max_digits=4,
        decimal_places=2,
    )
    left_thigh = models.DecimalField(
        verbose_name=_("Coxa esquerda"),
        max_digits=4,
        decimal_places=2,
    )
    right_calf = models.DecimalField(
        verbose_name=_("Panturrilha direita"),
        max_digits=4,
        decimal_places=2,
    )
    left_calf = models.DecimalField(
        verbose_name=_("Panturrilha esquerda"),
        max_digits=4,
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

    @property
    def bmi(self):
        # O Índice de Massa Corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal.
        # Categorias de IMC:
        # Abaixo do peso = <18,5
        # Peso normal = 18,5–24,9
        # Excesso de peso = 25–29,9
        # Obesidade = IMC de 30 ou mais

        cal = self.weight / (self.height * self.height)

        if cal < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= cal <= 24.9:
            return "Peso normal"
        elif 25 <= cal <= 29.9:
            return "Excesso de peso"
        else:
            return "Obesidade"

    @property
    def rcq(self):
        # A relação cintura-quadril (RCQ) é o cálculo que se faz a partir das medidas da cintura e do quadril para verificar o risco que uma pessoa tem de desenvolver uma doença cardiovascular.
        # Risco de saúde    Mulher              Homem
        # Baixo             Inferior a 0,80     Inferior a 0,95
        # Moderado          0,81 a 0,85         0,96 a 1,0
        # Alto Superior     0,86                Superior 1,0

        cal = self.waist / self.hip
        sex = self.user.sex

        if sex == "M":
            if cal < 0.80:
                return "Baixo"
            elif 0.80 <= cal <= 0.85:
                return "Moderado"
            else:
                return "Alto"
        elif sex == "H":
            if cal < 0.95:
                return "Baixo"
            elif 0.95 <= cal <= 1.0:
                return "Moderado"
            else:
                return "Alto"
        else:
            return "Sexo não reconhecido"

    def __str__(self):
        return f"{self.user} - {self.created_at}"

    class Meta:
        verbose_name = _("Medida")
        verbose_name_plural = _("Medidas")
        ordering = ["-created_at"]
