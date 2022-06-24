#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 18:56:07 2022
#========================================
from rest_framework import viewsets
from core.models import Project
from core.serializers import ProjectSerializer
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class ProjectViewSet(viewsets.ModelViewSet):
    '''
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
