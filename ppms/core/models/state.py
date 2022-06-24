#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 15:30:59 2022
#========================================
from django.db import models
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class State(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_states'

    #-
    name  = models.CharField(max_length=30)

    #-
    order = models.PositiveSmallIntegerField(unique=True)
    
    
    def __str__(self):
        '''
        '''
        return self.name
