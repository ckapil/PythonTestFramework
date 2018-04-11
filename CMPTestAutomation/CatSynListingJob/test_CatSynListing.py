import pytest
from DatabaseSetup import PBLDBConnection as pbldb
from Utils import DefaultProperties as dp
from Utils import PrepExpectedData as expData
from Utils import QADisplayTestResult as storeOutput
from Utils import PrepActualData as actualData


@pytest.fixture(scope="module")
def pbldbConn():
    # pbldb.server.start()
    pbldbConn = pbldb.dbConn()
    yield pbldbConn
    pbldbConn.close()
    # pbldb.server.stop()

def test_PriceValidation(pbldbConn):
    expectedDataFrame = expData.expectedDataPriceValidation(dp.currentRunningMerchant)
    skuNumbers = expectedDataFrame['Actual_SKU']
    actualDataFrame = actualData.getActualPriceValidationValues(pbldbConn, skuNumbers)
    storeOutput.final_data(expectedDataFrame, actualDataFrame, 'test_PriceValidation')
    for eachSKU in skuNumbers:
        expectedValues = expectedDataFrame[expectedDataFrame.Actual_SKU == eachSKU]
        actualValues = actualDataFrame[actualDataFrame.bfid == eachSKU]
        assert (expectedValues['Sale_Price'].values == actualValues['sale_price_value'].values)
        assert (expectedValues['Retail_Price'].values == actualValues['price_value'].values)
        assert (expectedValues['Currency'].values == actualValues['price_currency'].values)
    print("Test Passed: All values match")

def test_ItemStateValidation():
    print("test 2")


def test_InventoryValidation(pbldbConn):
    inventoryThresholdVal = actualData.getInventoryThresholdValue(pbldbConn,dp.currentRunningMerchant)
    expectedDataFrame = expData.expectedDataInventoryValidation(dp.currentRunningMerchant, inventoryThresholdVal.values)
    skuNumbers = expectedDataFrame['Actual_SKU']
    actualDataFrame = actualData.getActualInventoryValidationValues(pbldbConn, skuNumbers)
    for eachSKU in skuNumbers:
        expectedValues = expectedDataFrame[expectedDataFrame.Actual_SKU == eachSKU]
        actualValues = actualDataFrame[actualDataFrame.bfid == eachSKU]
        assert (expectedValues['Expected_Merchant_Quantity'].values == actualValues['quantity'].values)
    print ("Test Passed: All values match")


def test_TimeStampValidation():
    print('test 4')


def test_SizeChart():
    print('test 5')
