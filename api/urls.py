from rest_framework import routers
from . import views as api_views

router = routers.SimpleRouter()
router.register('task', api_views.HomeModelViewSet, basename="task")

urlpatterns = router.urls