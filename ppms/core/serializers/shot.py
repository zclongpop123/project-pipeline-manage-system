#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:50 2022
#========================================
from core.models import Shot
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class ShotSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = Shot
        fields = '__all__'
