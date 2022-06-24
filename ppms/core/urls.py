#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 18:58:57 2022
#========================================
from django.urls import include, path
from rest_framework import routers
from core import views
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
router = routers.DefaultRouter()
router.register('projects',  views.ProjectViewSet)
router.register('categorys', views.CategoryViewSet)
router.register('steps',     views.StepViewSet)
router.register('states',    views.StateViewSet)
router.register('assets',    views.AssetViewSet)
router.register('episodes',  views.EpisodeViewSet)
router.register('sequences', views.SequenceViewSet)
router.register('shots',     views.ShotViewSet)
router.register('tasks',     views.TaskViewSet)
router.register('versions',  views.VersionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]