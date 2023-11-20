from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.MyTokenObtainPairSerializer import MyTokenObtainPairSerializer


class MyTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
