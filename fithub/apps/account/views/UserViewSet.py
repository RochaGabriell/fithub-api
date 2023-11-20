from rest_framework import viewsets, permissions, response
from rest_framework.decorators import api_view, permission_classes

from fithub.apps.account.serializers.UserSerializer import UserSerializer, UserCreateSerializer, ProfileSerializer
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


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_profile(request):
    """
    Endpoint da API que permite que o perfil do usuário seja visualizado. (GET)
    """
    user = request.user
    serializer = ProfileSerializer(user)
    return response.Response(serializer.data)
