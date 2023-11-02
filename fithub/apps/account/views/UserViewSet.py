from rest_framework import viewsets, permissions

from fithub.apps.account.serializers.UserSerializer import UserSerializer, UserCreateSerializer
from fithub.apps.account.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os usuários sejam visualizados ou editados. (GET, PUT, PATCH, DELETE)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        # Se a ação for 'create', retorna o serializer de criação de usuário
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        # Se a ação for 'create', não é necessário estar autenticado
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
