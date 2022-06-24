#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 17:00:20 2022
#========================================
from django.db import models
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Step(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_steps'

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        '''
        '''
        return self.name
