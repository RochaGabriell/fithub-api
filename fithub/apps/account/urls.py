from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from django.urls import path

from fithub.apps.account.views import UserViewSet, MeasurementsViewSet

app_name = 'account'

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'measurements', MeasurementsViewSet)

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
