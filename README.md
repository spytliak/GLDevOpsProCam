for  "GL DevOps ProCamp"

The script prints basic information about OS to console.


Setup

docker build -t [NAME] .

Usage

docker run [NAME]

Example

root@serg:~/metrics/GLDevOpsProCam# docker run info
HOSTNAME: e6f3f248602e RELEASE: 4.15.0-91-generic VERSION: x86_64
Uptime: 8 days, 7 hours, 19 minutes, 05 seconds!
Local current time: Fri Mar 27 14:30:58 2020
----MEMORY----
virtual total 2089340928
virtual available 1473884160
virtual used 29.5
virtual free 447234048
virtual active 266256384
virtual inactive 823160832
virtual buffers 799961088
virtual cached 183263232
virtual shared 1192587264
virtual slab 2609152
virtual wired 164388864
swap total 1008726016
swap used 536576
swap free 1008189440
swap percent 0.1
----CPU----
system cpu user 964.77
system cpu system 81.73
system cpu idle 1414.0
system cpu iowait 2838157.97
system cpu guest 26053.89
system load average: (0.16, 0.05, 0.01)
-----Disks-----
device= /dev/sda2 mountpoint= /etc/resolv.conf fstype= ext4
device= /dev/sda2 mountpoint= /etc/hostname fstype= ext4
device= /dev/sda2 mountpoint= /etc/hosts fstype= ext4
Total: 21 GiB Used: 7 GiB Free: 12 GiB
----IP----
ip: ['172.17.0.2']
