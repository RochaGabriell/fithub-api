from rest_framework import serializers

from fithub.apps.account.models import Measurements


class MeasurementsSerializer(serializers.ModelSerializer):

    bmi = serializers.SerializerMethodField()
    rcq = serializers.SerializerMethodField()

    class Meta:

        model = Measurements
        fields = "__all__"

    def get_bmi(self, obj):
        # O Índice de Massa Corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal.
        # Categorias de IMC:
        # Abaixo do peso = <18,5
        # Peso normal = 18,5–24,9
        # Excesso de peso = 25–29,9
        # Obesidade = IMC de 30 ou mais

        cal = obj.weight / (obj.height * obj.height)

        if cal < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= cal <= 24.9:
            return "Peso normal"
        elif 25 <= cal <= 29.9:
            return "Excesso de peso"
        else:
            return "Obesidade"

    def get_rcq(self, obj):
        # A relação cintura-quadril (RCQ) é o cálculo que se faz a partir das medidas da cintura e do quadril para verificar o risco que uma pessoa tem de desenvolver uma doença cardiovascular.
        # Risco de saúde    Mulher              Homem
        # Baixo             Inferior a 0,80     Inferior a 0,95
        # Moderado          0,81 a 0,85         0,96 a 1,0
        # Alto Superior     0,86                Superior 1,0

        cal = obj.waist / obj.hip
        sex = obj.user.sex

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
