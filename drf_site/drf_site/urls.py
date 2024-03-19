from django.contrib import admin
from django.urls import path

from women.views import *

# роутеры лучше создавать в отдельных файлах

# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}§',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]
#
# # router = routers.SimpleRouter()
# # router = routers.DefaultRouter()
# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename='women')
# когда убираем queryset из WomenViewSet, нам нужно прописать basename

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls))
    # path('api/v1/womenlist', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>', WomenAPIDetailView.as_view()),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]
