import pandas as pd

def getActualPriceValidationValues(pbldbConn, skuNumbers):
    str = ""
    counter = skuNumbers.size
    for i in skuNumbers:
        str = str + "'" + i + "'"
        counter = counter - 1
        if counter > 0:
            str = str + ","
    query = "select bfid, price_value, sale_price_value, price_currency from pbl_cat_item where bfid in ( %s )" % (str)
    df = pd.read_sql_query(query, pbldbConn)
    # print (df)
    return df

def getActualInventoryValidationValues(pbldbConn, skuNumbers):
    str = ""
    counter = skuNumbers.size
    for i in skuNumbers:
        str = str + "'" + i + "'"
        counter = counter - 1
        if counter > 0:
            str = str + ","
    query = "select bfid, quantity, merchant_quantity from pbl_cat_item where bfid in (" + str + ")"
    df = pd.read_sql_query(query, pbldbConn)
    return df

def getInventoryThresholdValue (pbldbConn, merchantID):
    query = "SELECT inventory_threshold FROM pbl.pbl_product_type_inventory_threshold where bf_merchant_id=" + str(merchantID)
    invThreshold = pd.read_sql_query(query, pbldbConn)
    return invThreshold