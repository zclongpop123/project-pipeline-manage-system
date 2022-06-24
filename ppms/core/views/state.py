#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 18:56:07 2022
#========================================
from rest_framework import viewsets
from core.models import State
from core.serializers import StateSerializer
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class StateViewSet(viewsets.ModelViewSet):
    '''
    '''
    queryset = State.objects.all()
    serializer_class = StateSerializer
