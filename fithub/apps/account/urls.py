from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from django.urls import path

from fithub.apps.account.views import UserViewSet, LogoutViewSet, MeasurementsViewSet, MyTokenObtainPairViewSet
from fithub.apps.account.views.UserViewSet import get_profile

app_name = 'account'

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'measurements', MeasurementsViewSet)

urlpatterns = [
    path('token/', MyTokenObtainPairViewSet.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', get_profile, name='profile'),
    path('logout/', LogoutViewSet.as_view(), name='logout'),
] + router.urls
