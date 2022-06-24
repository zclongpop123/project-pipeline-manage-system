#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:49 2022
#========================================
from core.models import Sequence
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class SequenceSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = Sequence
        fields = '__all__'
