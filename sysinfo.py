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
