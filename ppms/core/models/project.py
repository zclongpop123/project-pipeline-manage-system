#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 15:21:55 2022
#========================================
from django.db import models
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Project(models.Model):
    '''
    '''
    class Meta:
        db_table = 'core_projects'

    #-
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    
    #-
    start_date = models.DateField(auto_now=True)
    end_date   = models.DateField(auto_now=True)

    #-
    fps = models.PositiveSmallIntegerField(default=24)


    def __str__(self):
        '''
        '''
        return self.name
