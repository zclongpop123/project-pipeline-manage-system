#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 15:49:17 2022
#========================================
from django.db import models
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Asset(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_assets'

    #-
    name  = models.CharField(max_length=30)

    #- 项目
    project  = models.ForeignKey('core.Project',  null=True, on_delete=models.SET_NULL)

    #- 分类
    category = models.ForeignKey('core.Category', null=True, on_delete=models.SET_NULL)

    #- 状态
    state    = models.ForeignKey('core.State',    null=True, on_delete=models.SET_NULL)


    def __str__(self):
        '''
        '''
        return self.name
