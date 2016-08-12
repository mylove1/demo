# -*- coding:utf-8 -*-
import psutil
import time
netinfo = []
net = psutil.net_io_counters()


while 1:

    net_recv = '{0:.2f} kb'.format(net.bytes_recv / 1024)
    net_send = '{0:.2f} kb'.format(net.bytes_sent / 1024)
    netinfo.append((net_recv, net_send))
    time.sleep(1)
