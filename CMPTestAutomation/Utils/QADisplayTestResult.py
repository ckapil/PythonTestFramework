import pandas as pd
import xlwt
import mysql.connector
from datetime import datetime
from Utils import DefaultProperties as dp
import os

'''
def dbConn():
    sql_hostname = 'cmqards-cluster.cluster-c9y71vfgfyv3.us-east-1.rds.amazonaws.com'
    sql_username = 'marketconadmin'
    sql_password = 'MarketCon#123'
    sql_main_database = 'pbl'
    sql_port = 3306
    conn = mysql.connector.connect(host=sql_hostname,
                                       user=sql_username,
                                       password=sql_password,
                                       database=sql_main_database,
                                       port=sql_port)
    return conn

def read_expected_result():
  df_expected = pd.read_csv('catalog-sup-2017-04-18-10-25-00.csv', '|', usecols=['SKU_Number', 'Retail_Price', 'Sale_Price', 'Currency'])
  df_expected['bfid'] = '3787-' + df_expected['SKU_Number'].astype(str)
  df_expected = df_expected[['bfid', 'Retail_Price', 'Sale_Price', 'Currency']]
  return df_expected



def read_actual_result():
    query = "select bfid, price_value, sale_price_value, price_currency from pbl_cat_item where bfid like '3787-%%'"
    df_actual = pd.read_sql_query(query, dbConn())
    return df_actual

'''

def final_data(expectedData, actualData, testName):
   df1 = expectedData
   df1['bfid'] = df1['Actual_SKU'].astype(str)
   df2 = actualData
   df_result = pd.merge(df1, df2, on='bfid', how='outer')
   df_result = df_result[['bfid', 'Retail_Price', 'price_value', 'Sale_Price', 'sale_price_value', 'Currency', 'price_currency']]
   df_result = df_result.rename(columns={'Retail_Price': 'Expected_Retail_Price', 'price_value': 'Actual_Retail_Price', 'Sale_Price': 'Expected_Sale_Price', 'sale_price_value': 'Actual_Sale_Price', 'Currency': 'Expected_Currency', 'price_currency': 'Actual_Currency'})
   if os.path.isdir(dp.testResultPath):
      testName = dp.testResultPath + testName + 'Output_' + str(dp.currentRunningMerchant) + '_' + datetime.now().strftime('%Y%m%d_%H%M%S')+ '.xlsx'
   else:
      os.mkdir(dp.testResultPath)
      testName = dp.testResultPath + testName + 'Output_' + str(dp.currentRunningMerchant) + '_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.xlsx'
   df_result.to_excel(testName)

#final_data()




