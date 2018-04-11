# PythonTestFramework
Python E2E test framework

Install latest version of Pycharm from: https://www.jetbrains.com/pycharm/download/#section=windows
Python version used for development: 3.4
Check out the code from Github: 
Look for requirements.txt at location "<local path>\CMP-Automation\CMPTestAutomation\”
Install all the packages mentioned in requirements.txt using command:
      pip install -r requirements.txt
This will install most of the packages that are required for running the automation suite. If you still get an error for a missing package then install it manually using command:
      pip install <package name>
Here is the Framework structure:
    •	CatSynListingJob: Contains controller script and the test script containing the test methods that are called from the controller script
    •	DatabaseSetup: Contains the scripts for creating database connections and resetting the database
    •	TestResult: Contains html test reports for each run. The test report is identified by a combination of type of test (eg: CatSynListing or TMALLOrderFlow) and date and time stamp. Eg: “CatSynListingTestReport_5418_20170710_051349.html”
    •	TMALLOrderFlow: Automation of Tmall order flow is in progress. After completion, there will be a controller script for controlling and triggering the execution and there will be a test script that would contain all the tests related to tmall order flow.
    •	Utils: Contains all the utility scripts: 
          i.	DefaultProperties.py: Contains all the environment related configurations and global variables
         ii.	CatSynJobEnd.py: Checks if the CatSynLIsting job is running on the env to be tested
        iii.	CopyInputFile.py: Copies the catalog file to sftp location
         iv.	PrepActualData.py: Returns a dataframe containing the actual data that has been pushed to database by the CatSynListing
          v.	PrepExpectedData.py: Returns a dataframe containing the expected values for the test.
         vi.	QADisplayTestResult.py: Dumps the expected and actual values for a test to a csv file. We might remove this in future as we are planning to add this to the html reports.
7.	QA Automation DB: The execution of the tests is controlled from a database. 
