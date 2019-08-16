# -*- coding=utf8 -*-
import os, time
import re

filepath = "/root/cmake.log"    #nohup编译过程日志
running_log = "/root/python_running.log"    #脚本输出日志
count = 1   #统计执行失败后重启编译的次数

while 1:
    fr = open(filepath, "r").read()
    fr.close()
    #判断编译日志中是否有因报错而失败的输出，如果有则自动再次编译
