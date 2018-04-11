from DatabaseSetup import PBLDBConnection as labsdb
import mysql.connector
import sys


# Function to get merchant id for which DB needs to be cleaned
def cleanDB(merchID):
    # Fetching the merchant from the calling script
    merchant_to_query = str(merchID)

    # Querying DB to get merchant status
    conn = labsdb.dbConn()
    cur = conn.cursor()
    query = "select status from pbl_mrc_merchant where bf_merchant_id = %s" % merchant_to_query
    cur.execute(query)

    # Getting merchant status from query result
    merch_status = cur.fetchone()

    # Calling cleanup function if merchant is enabled else exiting the program
    if (str(merch_status[0]) == 'ENABLED'):
        cleanDBSDB(merchant_to_query)
        # cleanDB(merchant_to_query)
        conn.close()
        return True

    else:
        conn.close()
        return False



# Function to clean db using pandas

def cleanDBSDB_test(merch_to_clean):
    # Formating merchant code for delete query
    merchName = str(merch_to_clean) + '-' + '%'

    # Creating DB Connection
    conn_clean = labsdb.dbConn()

    #Creating cursor
    cursor = conn_clean.cursor()

    #Multiple Queries
    clean_pbl_cat_item_custom_label = "delete from pbl_cat_item_custom_label where bfid like '%s'"
    clean_pbl_cat_item_product_type = "delete from pbl_cat_item_product_type where bfid like '%s'"
    clean_pbl_cat_item_additional_image = "delete from pbl_cat_item_additional_image where bfid like '%s'"
    clean_pbl_mkl_item_market_state = "delete from pbl_mkl_item_market_state where bfid like '%s'"
    #  clean_pbl_cat_item_country_hscode = "delete from pbl_cat_item_country_hscode where bfid like '%s'"
    clean_pbl_cat_item_country = "delete from pbl_cat_item_country where bfid like '%s'"
    clean_pbl_cat_item_group = "delete from pbl_cat_item_group where bfid like '%s'"
    clean_pbl_cat_item = "delete from pbl_cat_item where bfid like '%s'"


    # Creating query
    clean_merch_data = clean_pbl_cat_item_custom_label; clean_pbl_cat_item_product_type; clean_pbl_cat_item_additional_image; clean_pbl_mkl_item_market_state;clean_pbl_cat_item_country;clean_pbl_cat_item_group;clean_pbl_cat_item
    clean_pbl_running_job = "delete from pbl_running_job where job_name = 'CatSynListing'"

    # Deleting record from table
    cursor.executemany(clean_merch_data,merchName)
    cursor.execute(clean_pbl_running_job)

    # Committing the delete queries
    conn_clean.commit()

    # Closing DB connection
    conn_clean.close()


# Function to execute DB cleanup queries
def cleanDBSDB(merch_to_clean):
    # Formating merchant code for delete query
    merchName = str(merch_to_clean) + '-' + '%'

    # Creating DB Connection
    conn_clean = labsdb.dbConn()

    # Creating cursors for multipe DB queries
    cur_clean_pbl_cat_item_custom_label = conn_clean.cursor()
    cur_clean_pbl_cat_item_product_type = conn_clean.cursor()
    cur_clean_pbl_cat_item_additional_image = conn_clean.cursor()
    cur_clean_pbl_mkl_item_market_state = conn_clean.cursor()
    #   cur_clean_pbl_cat_item_country_hscode = conn_clean.cursor()
    cur_clean_pbl_cat_item_country = conn_clean.cursor()
    cur_clean_pbl_cat_item_group = conn_clean.cursor()
    cur_clean_pbl_cat_item = conn_clean.cursor()
    cur_clean_pbl_running_job = conn_clean.cursor()

    # List of queries for DB cleanups
    clean_pbl_cat_item_custom_label = "delete from pbl_cat_item_custom_label where bfid like '%s'"
    clean_pbl_cat_item_product_type = "delete from pbl_cat_item_product_type where bfid like '%s'"
    clean_pbl_cat_item_additional_image = "delete from pbl_cat_item_additional_image where bfid like '%s'"
    clean_pbl_mkl_item_market_state = "delete from pbl_mkl_item_market_state where bfid like '%s'"
    #  clean_pbl_cat_item_country_hscode = "delete from pbl_cat_item_country_hscode where bfid like '%s'"
    clean_pbl_cat_item_country = "delete from pbl_cat_item_country where bfid like '%s'"
    clean_pbl_cat_item_group = "delete from pbl_cat_item_group where bfid like '%s'"
    clean_pbl_cat_item = "delete from pbl_cat_item where bfid like '%s'"

    # Query to clean pbl running job table
    clean_pbl_running_job = "delete from pbl_running_job where job_name = 'CatSynListing'"

    # Executing delete queries on DB
    cur_clean_pbl_cat_item_custom_label.execute(clean_pbl_cat_item_custom_label % merchName)
    cur_clean_pbl_cat_item_product_type.execute(clean_pbl_cat_item_product_type % merchName)
    cur_clean_pbl_cat_item_additional_image.execute(clean_pbl_cat_item_additional_image % merchName)
    cur_clean_pbl_mkl_item_market_state.execute(clean_pbl_mkl_item_market_state % merchName)
    # cur_clean_pbl_cat_item_country_hscode.execute(clean_pbl_cat_item_country_hscode % merchName)
    cur_clean_pbl_cat_item_country.execute(clean_pbl_cat_item_country % merchName)
    cur_clean_pbl_cat_item_group.execute(clean_pbl_cat_item_group % merchName)
    cur_clean_pbl_cat_item.execute(clean_pbl_cat_item % merchName)
    cur_clean_pbl_running_job.execute(clean_pbl_running_job)

    # Committing the delete queries
    conn_clean.commit()

    # Closing DB connection
    conn_clean.close()


# getEnabledMerchant(3787, True)
#cleanDB(3787)
