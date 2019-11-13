#!/bin/python3

import os
import subprocess

def host_info():
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

def network_info():

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

def storage_info():
    get_vol_info = subprocess.getoutput("df -h")
    get_lvm_pv_info = subprocess.getoutput("pvs")
    get_lvm_vg_info = subprocess.getoutput("vgs")
    get_lvm_lv_info = subprocess.getoutput("lvs")
    get_fdisk_info = subprocess.getoutput("fdisk -l")
    get_fstab_info = subprocess.getoutput("/bin/cat /etc/fstab")
    #Add autofs info
    get_nfs_exports_info = subprocess.getoutput("/bin/cat /etc/exports")
    get_smb_conf_info = subprocess.getoutput("/bin/cat /etc/samba/smb.conf")
    get_iscsi_init_info = subprocess.getoutput("/bin/cat /etc/iscsi/initiatorname.iscsi")
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
    print (" ")
    print ("----- PV Info -----\n",get_lvm_pv_info)
    print (" ")
    print ("----- VG Info -----\n",get_lvm_vg_info)
    print (" ")
    print ("----- LV Info -----\n",get_lvm_lv_info)
    print (" ")
    print ("----- FDISK Info -----\n",get_fdisk_info)
    print (" ")
    print ("----- FSTAB Info -----\n",get_fstab_info)
    print (" ")
    print ("----- NFS Exports Info -----\n",get_nfs_exports_info)
    print (" ")
    print ("----- SMB Conf Info -----\n",get_smb_conf_info)
    print (" ")
    print ("----- ISCSI Init Info -----\n",get_iscsi_init_info)
    print (" ")
    print ("----- ISCSI DISCOVERY Info ------\n",get_iscsi_dscv_info)
    print (" ")
    print ("----- ISCSI IFACE INFO -----\n",get_iscsi_iface_info)
    print (" ")
    print (get_iscsi_iface_info)
    print (" ")
    print ("----- ISCSI SESSION Show Info -----\n",get_iscsi_session_show_info)
    print (" ")
    print ("----- ISCSI Node Info -----\n",get_iscsi_node_info)
    print (" ")
    print ("----- Multipath Info -----\n",get_multipath_info)
    print (" ")



def user_info(): 
    get_users = subprocess.getoutput("/bin/cat /etc/passwd")
    get_groups = subprocess.getoutput("/bin/cat /etc/group")
    get_sudoers = subprocess.getoutput("/bin/cat /etc/sudoer | grep -v \#")
    get_sudoers.d = subprocess.getoutput("/bin")
    
    print ("======================== User Info ========================")
    print (" ")
    print ("----- Users Info -----\n",get_users)
    print (" ")
    print ("----- Groups Info -----\n",get_groups)
    print (" ")



def system_misc():
    #get_active_ps = subprocess.getoutput("/bin/ps -ef  | grep -v root | grep -v xfs | grep -v sshd | grep -v bash | grep -v gdm | grep -v rpc | grep -v dbus | grep -v hald | grep -v ps | grep -v tee | grep -v mutt")
    get_active_ps = subprocess.getoutput("/bin/ps -ef | grep -vE 'ps|dbus|xfs|root|sshd|gdm|rpc|dns|chronyd|lsmd|polkitd|rtkit|avahi|qmgr|colord|pickup'")
    get_chkcfg_list = subprocess.getoutput("/sbin/chkconfig --list")
    get_systemctl = subprocess.getoutput("/usr/bin/systemctl")
    get_sysctl_conf = subprocess.getoutput("/bin/cat /etc/sysctl.conf")
    get_security_lmts = subprocess.getoutput("/bin/cat /etc/security/limits.conf | grep -v \#")

    print ("======================== System Misc. ========================")
    print (" ")
    print ("----- Active Processes -----\n",get_active_ps)
    print (" ")
    print ("----- Check Config List -----\n",get_chkcfg_list)
    print (" ")
    print ("----- Systemctl Info -----\n",get_systemctl)
    print (" ")
    print ("----- Security Limits Info -----\n",get_security_lmts)
    print (" ")


host_info()
network_info()
storage_info()
user_info()
system_misc()


#take all function output to a file, and to email. 
