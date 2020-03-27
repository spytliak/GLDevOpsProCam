#!/usr/bin/env python
# ---------------------------------------------------
# Program by Pytliak Serhii <pytliak.serhii@gmail.com>
# Version  Date       Info
# 1.0      26.03.20   System info - metrics
# ----------------------------------------------------
# -*- coding: utf-8 -*-
import psutil, sys, os, time, datetime


#Hostname
OS = os.uname()
print('HOSTNAME:', OS[1], 'RELEASE:', OS[2], 'VERSION:', OS[4])


#Uptime
MINUTES = 60
HOUR = MINUTES * 60
DAY = HOUR * 24
bootTIME = psutil.boot_time()
NOW = time.time()
s = NOW - bootTIME
d = h = m = 0
d = s / DAY
s = s % DAY
h = s / HOUR
s = s % HOUR
m = s / MINUTES
s = s % MINUTES
uptime = ""
if d > 1:
    uptime = "%d days, "%d
elif d == 1:
    uptime = "1 day, "
print("Uptime: " + uptime + "%d hours, %02d minutes, %02d seconds!"%(h,m,s))


#Localtime
localtime = time.asctime( time.localtime(time.time()) )
print ('Local current time:', localtime)


#users
for user in psutil.users():
    print('Authorized Users:', user.name, 'TTY', user.terminal, 'FROM', user.host)


#Memory
#psutil.virtual_memory()
#psutil.swap_memory()
def mem():
    print('----MEMORY----')
    mem_name = ['total', 'available', 'used', 'free', 'active', 'inactive', 'buffers', 'cached', 'shared', 'slab', 'wired']
    for name, value in zip(mem_name, psutil.virtual_memory()):
        print('virtual', name, value)
    swap_name = ['total', 'used', 'free', 'percent']
    for name, value in zip(swap_name, psutil.swap_memory()):
         print('swap', name, value)
mem()


#CPU
#psutil.cpu_times()
#psutil.getloadavg()
def cpu():
    print('----CPU----')
    cpu_name = ['user', 'system', 'idle', 'iowait', 'guest',]
    for name, value in zip(cpu_name, psutil.cpu_times()):
         print('system cpu', name, value)
cpu()
print('system load average:', psutil.getloadavg())


#Disks
#psutil.disk_partitions()
#psutil.disk_usage('/')
print('-----Disks-----')
for dp in psutil.disk_partitions():
    print('device=', dp.device, 'mountpoint=', dp.mountpoint, 'fstype=', dp.fstype )
du = psutil.disk_usage('/')
print ('Total: %d GiB' % (du.total / (2**30)),'Used: %d GiB' % (du.used / (2**30)),'Free: %d GiB' % (du.free / (2**30)))


#Network
#psutil.net_if_addrs()
#ip = psutil.net_if_addrs()
#print('The IP address is', ip)
def get_ips():
    print('----IP----')
    ifaces = psutil.net_if_addrs()
    ips = list()
    for iface, info in ifaces.items():
        if iface == 'lo':
            continue
        ip = info[0].address
        ips.append(ip)
    return ips
print('ip:', get_ips())

