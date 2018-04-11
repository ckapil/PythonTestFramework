import platform

currentOS = platform.platform()
runningEnv = 1 #For Staging Env assign 1 / For QA Env assign 0


if (runningEnv==1):
    # Staging Env config
    catsyn_hostname = '10.15.20.18'
    myntraexp_hostname = '10.15.20.109'
    pbldb_main_database = 'pbl'
else:
    # QA Env config
    catsyn_hostname = '10.15.20.5'
    myntraexp_hostname = '10.15.20.5'
    pbldb_main_database = 'pbl_qa'

# PBL Database Connection
pbldb_hostname = 'cmqards-cluster.cluster-c9y71vfgfyv3.us-east-1.rds.amazonaws.com'
pbldb_username = 'marketconadmin'
pbldb_password = 'MarketCon#123'
pbldb_main_database = 'pbl'

# QA Automation DB Connection
qadb_hostname = 'cmqards-cluster.cluster-c9y71vfgfyv3.us-east-1.rds.amazonaws.com'
qadb_username = 'marketconadmin'
qadb_password = 'MarketCon#123'
qadb_main_database = 'qaautomation'

# Merchant ID
merchantID = [5418]
currentRunningMerchant = 0

########################################CatSynListing Job parameters#############################

# Input Catalog feed path
inputCatalogPath = ""
if currentOS.__contains__("Windows"):
    inputCatalogPath = "..\\Utils\\"
else:
    inputCatalogPath = "/usr/automation/CMP-Automation/CMPTestAutomation/Utils/"

# CatSynListing Job config
catsyn_username = "ec2-user"
catsyn_privateKey = ""
if currentOS.__contains__("Windows"):
    catsyn_privateKey = "..\\Utils\\catsynd-dev.pem"
else:
    catsyn_privateKey = "/usr/automation/CMP-Automation/CMPTestAutomation/Utils/catsynd-dev.pem"

# Test Report Path
if currentOS.__contains__("Windows"):
    testResultPath = "..\\TestResult\\"
else:
    testResultPath = "/usr/automation/CMP-Automation/CMPTestAutomation/TestResult/"

########################################Myntra Order Flow parameters#############################
#No of orders to be created
no_of_orders = 50

#Save Order API endpoint
url = "http://10.15.20.109:8085/order/v1/"

#API credentials
userName = 'MyntraAPIUser'
pwd = 'Myntra12!'

#Active SKU
activeSKU = ""

#Myntra Exporter Config
myntraexp_username = "ec2-user"
myntraexp_privateKey = ""
if currentOS.__contains__("Windows"):
    myntraexp_privateKey = "..\\Utils\\MyntraAWSMachinepem.pem"
else:
    myntraexp_privateKey = "/usr/automation/CMP-Automation/CMPTestAutomation/Utils/MyntraAWSMachinepem.pem"

