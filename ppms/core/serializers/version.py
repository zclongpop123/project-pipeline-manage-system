#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:57 2022
#========================================
from core.models import Version
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class VersionSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = Version
        fields = '__all__'
