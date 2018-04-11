#import logging
#import sys
import mysql.connector as sqlconn
from Utils import DefaultProperties as dp

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

'''
from sshtunnel import SSHTunnelForwarder

qadbKey = dp.qadbKey

sql_hostname = '127.0.0.1'
sql_username = dp.pbldb_username
sql_password = dp.pbldb_password
sql_main_database = 'pbl'
sql_port = 3306
ssh_host = dp.pbldb_hostname
ssh_user = 'ec2-user'
ssh_port = 22

server = SSHTunnelForwarder(
             (ssh_host, ssh_port),
             ssh_username=ssh_user,
             ssh_pkey=qadbKey,
             remote_bind_address=(sql_hostname, sql_port)
 )

def dbConn():
     conn = sqlconn.connect(host=sql_hostname,
                            user=sql_username,
                            password=sql_password,
                            database=sql_main_database,
                            port= server.local_bind_port)
     return conn

'''


sql_hostname = dp.pbldb_hostname
sql_username = dp.pbldb_username
sql_password = dp.pbldb_password
sql_main_database = dp.pbldb_main_database

def dbConn():
    conn = sqlconn.connect(host = sql_hostname,
                           user = sql_username,
                           password = sql_password,
                           database = sql_main_database,
                           )
    return conn
