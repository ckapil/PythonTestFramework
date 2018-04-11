import pandas as pd
from Utils import DefaultProperties as dp

def expectedDataPriceValidation(merchantID):
    catalogPath = dp.inputCatalogPath + str(merchantID) + "_catalog.csv"
    df = pd.read_csv(catalogPath, '|', usecols=['SKU_Number', 'Retail_Price', 'Sale_Price', 'Currency'])
    df['Actual_SKU'] = str(merchantID) + "-" + df['SKU_Number'].astype(str)
    return df

def expectedDataInventoryValidation (merchantID, invThreshold):
    catalogPath = dp.inputCatalogPath + str(merchantID) + "_catalog.csv"
    df = pd.read_csv(catalogPath, '|', usecols=['SKU_Number','Qty_On_Hand'])
    df['Actual_SKU'] = str(merchantID) + "-" + df['SKU_Number'].astype(str)
    df['Expected_Merchant_Quantity'] = df['Qty_On_Hand'].astype(int) - int(invThreshold)
    return df

#testdf = expectedDataPriceValidation(3787)
#testdf = expectedDataInventoryValidation(3787, 7)
#print (testdf)

