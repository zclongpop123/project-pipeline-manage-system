#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 15:56:09 2022
#========================================
from django.db import models
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Category(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_categorys'

    #-
    name  = models.CharField(max_length=30)


    def __str__(self):
        '''
        '''
        return self.name
