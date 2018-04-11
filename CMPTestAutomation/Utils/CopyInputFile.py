import os
import paramiko
from DatabaseSetup import PBLDBConnection as labsdb
from Utils import DefaultProperties as dp


def getSFTPInfo(merchantID):
    conn = labsdb.dbConn()
    cur = conn.cursor()
    query = "select data_feed_host, data_feed_port, data_feed_user, data_feed_password, data_feed_remote_directory from pbl_mrc_merchant where bf_merchant_id =" + "'" + str(merchantID) + "'"
    cur.execute(query)
    row = cur.fetchone()
    host_from_db = row[0]
    port_from_db = row[1]
    username_from_db = row[2]
    password_from_db = row[3]
    remote_directory_db = row[4]
    conn.close()
    return (host_from_db, port_from_db, username_from_db, password_from_db, remote_directory_db)


def copy_catalog_file_to_sftp(merchantID):
    host, port, username, password, remoteDirectory = getSFTPInfo(merchantID)
    transport = paramiko.Transport(host, port)
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    remotePath = remoteDirectory + '/catalog-sup.csv'
    localPath = dp.inputCatalogPath + str(merchantID) + "_catalog.csv"
    if os.path.isfile(localPath):
        sftp.put(localPath, remotePath)
    else:
        print("File Not not found: " + localPath)
    sftp.close()
    transport.close()



#copy_catalog_file_to_sftp(5418)
