#!/bin/python3

import os
import subprocess

def host_info()
    get_hostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE)
    hostname = subprocess.getoutput("hostname")
    date = subprocess.getoutput("date +%Y%m%d-%H%M%S")
    os_version = subprocess.getoutput("/bin/cat /etc/*release")
    kernel_ver = subprocess.getoutput("uname -r")
    platform = subprocess.getoutput("uname -m")
    uptime = subprocess.getoutput("uptime | awk '{ print $2,$3,$4}'")

    print ("====================== Host Information =============================")
    print (" ")
    print ("Hostname:", hostname)
    print ("OS Version: ",date)
    print ("Kernel: ",kernel_ver)
    print ("Platform: ",platform)
    print ("Uptime: ",uptime )
    print (" ")

def network_info()

    #IFCONFIG
    get_ip_info = subprocess.getoutput("ip a")
    #DNS
    get_dns_info = subprocess.getoutput("/bin/cat /etc/resolv.conf")
    #NETSTAT
    get_route_info = subprocess.getoutput("/bin/netstat -nr")

    print ("====================== Network and IP Information ===================")
    print (" ")
    print ("----- IP Information -----\n",get_ip_info)
    print (" ")
    print ("----- DNS Server Info -----\n",get_dns_info)
    print (" ")
    print ("----- Host Route Info -----\n",get_route_info)
    print (" ")

def storage_info()
    get_vol_info = subprocess.getoutput("df -h")
    get_lvm_pv_info = subprocess.getoutput("pvs")
    get_lvm_vg_info = subprocess.getoutput("vgs")
    get_lvm_lv_info = subprocess.getoutput("lvs")
    get_fdisk_info = subprocess.getoutput("fdisk -l")
    get_fstab_info = subprocess.getoutput("/bin/cat /etc/fstab")
    #Add autofs info
    get_nfs_exports_info = subprocess.getoutput("/bin/cat /etc/exports")
    get_smb_conf_info = subprocess.getoutput("/bin/cat /etc/samba/smb.conf")
    get_isci_init_info = subprocess.getoutput("/bin/cat /etc/iscsi/initiatorname.iscsi")
    get_iscsi_dscv_info = subprocess.getoutput("/sbin/iscsiadm -m discovery -o show")
    get_iscsi_iface_info = subprocess.getoutput("/sbin/isciadmin -m iface")
    get_iscsi_iface2_info = subprocess.getoutput("/sbin/isciadmin -m iface -P 1")
    get_iscsi_session_show_info = subprocess.getoutput("/sbin/iscsiadmin -m session -o show")
    get_iscsi_session_info = subprocess.getoutput("/sbin/iscsiadm -m session -P3")
    get_iscsi_node_info = subprocess.getoutput("/sbin/iscsiadm -m node -o show | grep -iv empty")
    get_multipath_info = subprocess.getoutput("/sbin/multipath -ll")

    print ("======================== Storage Information ========================")
    print (" ")
    print ("----- Volume Info -----\n",get_vol_info)
#DF

#PVS
#VGS
#LVS
#FDISK 
#FSTAB
#NFS

def user_info() 

#Users
#Groups
#Sudoers



host_info()
network_info()
storage_info()
user_info()



#take all function output to a file, and to email. 
