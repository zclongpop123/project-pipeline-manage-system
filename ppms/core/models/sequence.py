#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 16:12:00 2022
#========================================
from django.db import models
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Sequence(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_sequences'

    #-
    name  = models.CharField(max_length=30)

    #- 项目
    project  = models.ForeignKey('core.Project',  null=True, on_delete=models.SET_NULL)

    #- 状态
    state    = models.ForeignKey('core.State',    null=True, on_delete=models.SET_NULL)


    def __str__(self):
        '''
        '''
        return self.name
