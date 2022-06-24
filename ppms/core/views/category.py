#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 18:56:07 2022
#========================================
from rest_framework import viewsets
from core.models import Category
from core.serializers import CategorySerializer
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class CategoryViewSet(viewsets.ModelViewSet):
    '''
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
