#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 18:56:07 2022
#========================================
from rest_framework import viewsets
from core.models import Task
from core.serializers import TaskSerializer
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class TaskViewSet(viewsets.ModelViewSet):
    '''
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
