import paramiko
from Utils import DefaultProperties as dp
#import logging
#import sys
import os

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def SSHCon(hostid,uid,key):
    k = paramiko.RSAKey.from_private_key_file(key)
    ssh_conn = paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.connect(hostname=hostid, username=uid, pkey=k)
    return ssh_conn

def exec_catsynlisting():
    commands = 'cd /usr/etl; ./catsynclisting.sh'
    (stdin, stdout, stderr) = SSHCon(dp.catsyn_hostname, dp.catsyn_username, dp.catsyn_privateKey).exec_command(commands, get_pty=True)
    SSHCon(dp.catsyn_hostname, dp.catsyn_username, dp.catsyn_privateKey).close()

def exec_mpexporter():
    commands = 'cd /usr/etl; ./mp_exporter.sh'
    (stdin, stdout, stderr) = SSHCon(dp.catsyn_hostname, dp.catsyn_username, dp.catsyn_privateKey).exec_command(commands, get_pty=True)
    SSHCon(dp.catsyn_hostname, dp.catsyn_username, dp.catsyn_privateKey).close()

def exec_unixCmd():
    commands = 'cd /usr/etl; ./catsynclisting.sh'
    os.system(commands)

def exec_myntraexporter():
    commands = 'cd /usr/etl; ./myntra_exporter.sh'
    (stdin, stdout, stderr) = SSHCon(dp.myntraexp_hostname, dp.myntraexp_username, dp.myntraexp_privateKey).exec_command(commands, get_pty=True)
    SSHCon().close()



#exec_myntraexporter()

#exec_catsynlisting()
