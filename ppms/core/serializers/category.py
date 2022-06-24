#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 23:01:41 2022
#========================================
from core.models import Category
from rest_framework import serializers
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class CategorySerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        '''
        '''
        model = Category
        fields = '__all__'
