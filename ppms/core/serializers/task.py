#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:56 2022
#========================================
from core.models import Task
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class TaskSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = Task
        fields = '__all__'
