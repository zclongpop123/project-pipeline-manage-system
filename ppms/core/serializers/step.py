#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:54 2022
#========================================
from core.models import Step
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class StepSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = Step
        fields = '__all__'
