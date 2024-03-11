from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from women.views import *

# роутеры лучше создавать в отдельных файлах

class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}§',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]

# router = routers.SimpleRouter()
# router = routers.DefaultRouter()
router = MyCustomRouter()
router.register(r'women', WomenViewSet, basename='women')
# когда убираем queryset из WomenViewSet, нам нужно прописать basename

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('api/v1/womenlist', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>', WomenAPIDetailView.as_view()),
]
