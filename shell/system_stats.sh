#!/bin/bash

hostname="`hostname`"
date="`date "+%Y%m%d-%H%M%S"`"

echo
(
echo "====================== Host Information ============================="
echo "  "
echo "Hostname: " $hostname
echo "OS Version: " `/bin/cat /etc/*release`
echo "Kernel: " `uname -r`
echo "Platform: " `uname -m`
echo "Uptime: " `uptime | awk '{ print $2,$3,$4 }'`
echo " "

# ifconfig
echo "============== IP Information (ifconfig -a) ================="
echo "  "
/sbin/ifconfig -a
echo "  "

#DNS Settings
echo "================= DNS Servers (resolv.conf) ================="
echo " "
/bin/cat /etc/resolv.conf
echo " "

# netstat -nr
echo "============ Network Host Routes (netstat -nr) ==============ls"
echo "  "
/bin/netstat -nr
echo "  "

# df -h
echo "============== Disk and Volume Space (df -h) ================"
echo "  "
/bin/df -h
echo "  "

# PVS DUMP
echo "================= PVS DUMP (/usr/sbin/pvs) =================="
echo " "
/usr/sbin/pvs
echo " "

# VGS DUMP
echo "================= VGS DUMP (/usr/sbin/vgs) =================="
echo " "
/usr/sbin/vgs
echo " "

# LVS DUMP
echo "================== LVS DUMP (/usr/sbin/lvs) ================="
echo " "
/usr/sbin/lvs
echo " "

# FDISK DUMP
echo "================== FDISK (/sbin/fdisk -l) ================="
echo " "
/sbin/fdisk -l
echo " "

# fstab
echo "============== Disk Volume Mounts (/etc/fstab) =============="
echo "  "
/bin/cat /etc/fstab
echo "  "

# SAMBA Configuration
echo "========= SAMBA Configuration (/etc/samba/smb.conf) =============="
echo " "
/bin/cat /etc/samba/smb.conf
echo " "

# NFS Configuration
echo "=============== NFS Configuration (/etc/exports) ================"
echo " "
/bin/cat /etc/exports

# Users and Groups
echo "============== User Account (/etc/passwd) ================="
echo " "
/bin/cat /etc/passwd
echo " "

echo "================ Groups (/etc/group) ==============="
echo " "
/bin/cat /etc/group
echo " "

# List of services running - postfix, nfs, apache tom/bin/cat - filtered ps -ef
echo "============= Running/Active Services (ps -ef) =============="
echo "  "
/bin/ps -ef | grep -v root | grep -v xfs | grep -v sshd | grep -v bash | grep -v gdm | grep -v rpc | grep -v dbus | grep -v hald | grep -v "ps -ef" | grep -v tee | grep -v mutt
echo "  "

# Check config output
echo "============ Startup Services (chkconfig --list) ============"
echo "  "
/sbin/chkconfig --list
echo "  "

# Check systemctl for RHEL 7 or higher
echo "====== Systemctl Loaded and Active Services (systemctl) ====="
echo " "
/usr/bin/systemctl
echo " "

# System Control Configuration
echo "================= Sysctl (/etc/sysctl.conf) =================="
echo " "
/bin/cat /etc/sysctl.conf
echo " "

# System Security Limits Configuration
echo "====== System Security Limits (/etc/security/limits.conf) ======"
echo " "
/bin/cat /etc/security/limits.conf
echo " "

# Multipath Configuration
echo "=========== Multipath.conf (/etc/multipath.conf) ==========="
echo " "
/bin/cat /etc/multipath.conf
echo " "

# Multipath
echo "================ Multipath (multipath -ll) ================="
echo " "
/sbin/multipath -ll
echo " "

# ISCSI data
echo "=== ISCSI Initiator Name (/etc/iscsi/initiatorname.iscsi) ==="
echo "  "
/bin/cat /etc/iscsi/initiatorname.iscsi
echo "  "

echo "==== ISCSI DISCOVERY INFO (iscsiadm -m discovery -o show) ==="
echo " "
/sbin/iscsiadm -m discovery -o show
echo " "

echo "============= ISCSI IFACE (iscsiadm -m iface) ==============="
echo " "
/sbin/iscsiadm -m iface
echo " "
/sbin/iscsiadm -m iface -P 1
echo " "

echo "====== ISCSI SESSION SHOW (iscsiadm -m session -o show) ======="
echo " "
/sbin/iscsiadm -m session -o show
echo " "

echo "========== ISCSI SESSION Info (iscsiadm -m session -P3) ========="
echo " "
/sbin/iscsiadm -m session -P3
echo " "

echo "========== ISCSI NODE Info (iscsiadm -m node -o show) ==========="
echo " "
/sbin/iscsiadm -m node -o show | grep -iv empty
echo " "


echo "========================= END DUMP =========================="
) | /usr/bin/tee /home/hhakeem/"$hostname"_system_stats_"$date".txt \ | /bin/mailx -s "System Stats for $hostname - $date." hamzah.hakeem@duke.edu
