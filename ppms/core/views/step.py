#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 18:56:07 2022
#========================================
from rest_framework import viewsets
from core.models import Step
from core.serializers import StepSerializer
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class StepViewSet(viewsets.ModelViewSet):
    '''
    '''
    queryset = Step.objects.all()
    serializer_class = StepSerializer
