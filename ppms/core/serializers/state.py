#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:52 2022
#========================================
from core.models import State
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class StateSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = State
        fields = '__all__'
