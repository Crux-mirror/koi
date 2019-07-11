#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "crux"  
#HomePage:http://blog.csdn.net/jacson_bai  
#FileName: *.py  
#Version:1.0.0
#des:注册modles
#====#====#====#====
import xadmin
from .models import AuxiliaryProfile,Scenarios,Example

#xadmin中这里是继承object，不再是继承admin
class AuxiliaryProfileAdmin(object):
    #显示的列
    list_display = ['name']
    #搜索的字段
    search_fields = ['name']
    #过滤
    list_filter = []

#注册助词使用场景 短语
class ScenariosAdmin(object):
    #显示的列
    list_display = ['scene','remark','sort']
    #搜索的字段
    search_fields = ['scene']
    #过滤
    list_filter = []


#xadmin中这里是继承object，不再是继承admin
class ExampleAdmin(object):
    #显示的列
    list_display = ['case','translate']
    #搜索的字段
    search_fields = ['case','translate']
    #过滤
    list_filter = []



xadmin.site.register(AuxiliaryProfile, AuxiliaryProfileAdmin)
xadmin.site.register(Scenarios,ScenariosAdmin)
xadmin.site.register(Example,ExampleAdmin)