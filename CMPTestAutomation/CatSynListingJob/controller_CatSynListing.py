import sys
from datetime import datetime

import pandas as pd
import pytest
from DatabaseSetup import QAAutoDBConn as qadb, CleanUpDB as cdb
from Utils import CheckCatSynJobEnd as jobStatus
from Utils import CopyInputFile as cpfile
from Utils import DefaultProperties as dp
from Utils import SSHConn


def getValidScenarios():
    conn = qadb.qadbConn()
    testScenarios = pd.read_sql_query('select SuiteName from catsynlisting', conn)
    conn.close()
    return testScenarios.values


def getTestScenarioDetails(suiteName):
    conn = qadb.qadbConn()
    query = "Select * from catsynlisting where SuiteName=" + "'" + suiteName + "'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def checkUserEnteredSuiteName(userEnteredSuite, validSuiteNames):
    for i in validSuiteNames:
        if i == userEnteredSuite:
            return True
    return False


def getTestsToExecute(scenarioDetails):
    testsToExecute = []
    cols = scenarioDetails.columns
    for i, row in scenarioDetails.iterrows():
        for col in cols:
            if not (col == 'ID' or col == 'SuiteName' or row[col] == 0):
                testsToExecute.append("test_" + col)
    return testsToExecute


def executeTests(testsToExecute):
    print(testsToExecute)
    testCommand = ""
    counter = len(testsToExecute)
    for test in testsToExecute:
        testCommand = testCommand + test
        counter = counter - 1
        if (counter > 0):
            testCommand = testCommand + " or "
    htmlReportName = '--html=' + dp.testResultPath + 'CatSynListingTestReport_' + str(dp.currentRunningMerchant) + '_' + datetime.now().strftime(
        '%Y%m%d_%H%M%S') + '.html'
    pytest.main(['-k', testCommand, htmlReportName])


def main():
    validSuiteNames = getValidScenarios()
    if len(sys.argv) < 2:
        print('Please enter a valid suite name. Here are the possible options: ' + validSuiteNames)
        sys.exit(1)

    for eachMerchant in dp.merchantID:
        dp.currentRunningMerchant = eachMerchant
        if (cdb.cleanDB(eachMerchant) == False):
            sys.exit(1)
        cpfile.copy_catalog_file_to_sftp(eachMerchant)
        SSHConn.exec_catsynlisting()
        if (jobStatus.checkJobEnd() == 0):
            print('The CatSynListing job failed')
            sys.exit(1)
        #inputVal = input('Enter the suite name you want to execute: ')
        inputVal = sys.argv[1]
        if not checkUserEnteredSuiteName(inputVal, validSuiteNames):
            print('Please enter a valid suite name from the following: ' + validSuiteNames)
            sys.exit(1)
        scenarioDetails = getTestScenarioDetails(inputVal)
        testsToExecute = getTestsToExecute(scenarioDetails)
        executeTests(testsToExecute)


if __name__ == '__main__':
    main()
