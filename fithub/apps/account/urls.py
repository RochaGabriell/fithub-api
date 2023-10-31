from rest_framework.routers import DefaultRouter

app_name = 'account'

router = DefaultRouter(trailing_slash=False)
router.register()

urlpatterns = router.urls
