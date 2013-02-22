# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models


class Todos(models.Model):
    '''待办任务
    '''
    title = models.CharField(u'内容', max_length=100)
    done = models.BooleanField(u'是否完成')

    class Meta:
        verbose_name = u'待办任务'

    def __unicode__(self):
        return u'%s---%s' % (self.title, self.done)

admin.site.register(Todos)
