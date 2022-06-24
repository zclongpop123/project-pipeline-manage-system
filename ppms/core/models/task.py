#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 15:17:29 2022
#========================================
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Task(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_tasks'

    name = models.CharField(max_length=30)

    #- 项目
    project = models.ForeignKey('core.Project',  null=True, on_delete=models.SET_NULL)

    #-
    parent_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
    parent_id   = models.PositiveIntegerField()
    parent      = GenericForeignKey('parent_type', 'parent_id')

    #- 环节
    step    = models.ForeignKey('core.Step',     null=True, on_delete=models.SET_NULL)


    def __str__(self):
        '''
        '''
        return self.name
