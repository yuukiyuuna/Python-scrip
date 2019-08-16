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
    if re.search("Configuring incomplete, errors occurred", fr) and \
            re.search("CMake Error at cmake/boost.cmake", fr):
        #执行shell命令（此处为编译mysql的命令）
        os.system("cd /software/mysql-8.0.17/build && \
                    nohup cmake .. -DCMAKE_INSTALL_PREFIX=/opt/mysql-8.0.17 \
                        -DMYSQL_DATADIR=/opt/mysql-8.0.17/date -DSYSCONFDIR=/etc \
                        -DSYSCONFDIR=/etc \
                        -DWITH_MYISAM_STORAGE_ENGINE=1 \
                        -DWITH_INNOBASE_STORAGE_ENGINE=1 \
                        -DWITH_MEMORY_STORAGE_ENGINE=1 \
                        -DWITH_READLINE=1 \
                        -DMYSQL_TCP_PORT=3306 \
                        -DENABLED_LOCAL_INFILE=1 \
                        -DWITH_PARTITION_STORAGE_ENGINE=1 \
                        -DEXTRA_CHARSETS=all \
                        -DDEFAULT_CHARSET=utf8 \
                        -DDEFAULT_COLLATION=utf8_general_ci \
                        -DDOWNLOAD_BOOST=1 \
                        -DWITH_BOOST=/usr/local/boost \
                        > /root/cmake.log 2>&1 &")
        #记录脚本输出日志
        open(running_log, "a").write("this scripts has been running count is " + str(count) + '\n')
        #次数统计
        count += 1
    #每3分钟判断一次
    time.sleep(180)
