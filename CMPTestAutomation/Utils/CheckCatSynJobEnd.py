import time
import pandas as pd
from DatabaseSetup import PBLDBConnection as labsdb


def checkDBEntry():
    query = "select * from pbl_running_job where job_name = 'CatSynListing'"
    conn = labsdb.dbConn()
    df = pd.read_sql_query(query, conn)
    row_count = len(df.axes[0])
    print(row_count)
    conn.close()
    return row_count


def checkJobEnd():
    counter = 0
    while (checkDBEntry()>0):
        if counter<10:
            time.sleep(30)
            counter = counter + 1
        else:
            return 0
    return 1



#print("Job run has ended")


#checkJobEnd()



