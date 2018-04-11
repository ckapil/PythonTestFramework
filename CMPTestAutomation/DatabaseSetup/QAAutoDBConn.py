#import logging
#import sys
import mysql.connector
from Utils import DefaultProperties as dp

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

sql_hostname = dp.qadb_hostname
sql_username = dp.qadb_username
sql_password = dp.qadb_password
sql_main_database = dp.qadb_main_database


def qadbConn():
    conn = mysql.connector.connect(host = sql_hostname,
                                   user = sql_username,
                                   password = sql_password,
                                   database = sql_main_database,
                                   )
    return conn