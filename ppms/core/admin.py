#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Fri Jun 24 16:01:25 2022
#========================================
from django.contrib import admin
from .models import Project, Category, Step, State, Asset, Sequence, Episode, Shot, Task, Version
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Step)
admin.site.register(State)
admin.site.register(Asset)
admin.site.register(Sequence)
admin.site.register(Episode)
admin.site.register(Shot)
admin.site.register(Task)
admin.site.register(Version)
