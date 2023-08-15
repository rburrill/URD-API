import requests
from requests_ntlm import HttpNtlmAuth
from datetime import date
import pandas as pd

# Authentication Credentials for API Call  
data = pd.read_csv("C:\\TestResults\\PythonCredentialFile.csv")                
username = data['username'].iloc[0]
password = data['password'].iloc[0]

# Class Accessible Variables
today = date.today().strftime("%Y-%m-%d")


def core_SyncControllerApiCalls():
	# API Call for /api/CoreSyncController/InsertEids
	# Takes a list of PhoneNumber and inserts those tdns into the wfl_Endpoint table and creates queue items where necessary.
	myJson = [
	  	{
		    "id": 0,
		    "crmId": 1,
		    "eid": "1234567891",
		    "rdId": "123456781",
		    "lastActivityDt": today,
		    "firstHeartbeatDt": today,
		    "registrationDt": today,
		    "isMarkedForDelete": 'false',
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today
	  	}
	]
	
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/InsertEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/CoreSyncController/DeleteEids
	# Takes a list of tdns and deletes those tdns from the wfl_Endpoint table or creates a terminate queue item.
	myJson = [
	  "1234567891"
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/DeleteEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/CoreSyncController/UpdateEids
	# Takes a list of CrmEidCombo and updates the crmId in the wfl_Endpoint table and generates queue items where necessary.
	myJson = [
  		{
    		"eid": "1234567891",
     		"crmId": 1
  		}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/UpdateEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/CoreSyncController/InsertEmergencyAddresses
	# Takes a list of CrmEidCombo and updates the crmId in the wfl_Endpoint table and generates queue items where necessary.
	myJson = [
  		{
		    "eid": "1234567891",
		    "streetAddress": "1234 URD Street",
		    "streetAddressAdditionalInformation": "APT 1",
		    "city": "Nowhere",
		    "stateCode": "UT",
		    "zip5": "84000",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today
	    }
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/InsertEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/CoreSyncController/UpdateEmergencyAddresses
	# Takes a list of CoreSyncEmergnecyAddresses and will update records in the dat_RegisteredAddress table.
	myJson = [
		{
		    "eid": "1234567891",
		    "streetAddress": "4321 URD Street",
		    "streetAddressAdditionalInformation": "APT 2",
		    "city": "Somewhere",
		    "stateCode": "UT",
		    "zip5": "84001",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today
		}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/UpdateEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/CoreSyncController/DeleteEmergencyAddresses
	# Takes a list of Eids and will remove records from the dat_RegisteredAddress table.
	myJson = [
			"1234567891"
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/DeleteEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
		# API Call for /api/CoreSyncController/InsertCoreAgreements
		# Inserts All new Core User Agreements
	myJson = [
		{
		    "id": 0,
		    "crmId": 1,
		    "agreement_Id": 9,
		    "oldestAgreementDt": today,
		    "createdDt": today,
		    "sourceCreatedDt": today,
		    "modifiedDt": today,
		    "sourceModifiedDt": today
		}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/InsertCoreAgreements", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)

		
def incomingDataRollsDownhill():
	# API Call for /api/IncomingDataRollsDownhillController/UpdateUrdAgreements
	# Update the user agreements in dat_UserDocument and set the Consent and SelfCert dates in dat_Person if they don't exist.
	myJson = {
	  "crmId": 1,
	  "coreUserId": 0,
	  "consentAgreement_Id": 9,
	  "consentCreatedDt": today,
	  "consentModifiedDt": today,
	  "selfCertificationAgreement_Id": 10,
	  "selfCertificationCreatedDt": today,
	  "selfCertificationModifiedDt": today
	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateUrdAgreements", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId
	# CoreUserHasNullCrmId will create an Endpoint with the Eid if it doesn't exist and a CrmId task if it doesn't exist.
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId?Eid=1234567891&CoreUserId=0", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IncomingDataRollsDownhillController/UpdateEmergencyAddress
	# UpdateEmergencyAddress will insert, delete or update an Emergency address to match the data passed into the method.
	myJson = {
	  "eids": [
	    "1234567891"
	  ],
	  "streetAddress": "1234 Testing Street",
	  "streetAddressAdditionalInformation": "APT 1",
	  "city": "Nowhere",
	  "stateCode": "UT",
	  "zip5": "84000",
	  "isProvisioned": 'true',
	  "sourceCreatedDt": today,
	  "sourceModifiedDt": today
	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEmergencyAddress", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/IncomingDataRollsDownhillController/UpdateCoreUser
	# Updates the Endpoints Crm information based on a list of eids, or inserts them as new endpoints if they don't already exist. 
	# Queue and Task items are created based upon what is inserted, deleted or updated.
	myJson = {
	  "coreUserId": 0,
	  "crmId": 1,
	  "eids": [
	    {
	      "coreUserId": 0,
	      "crmId": 1,
	      "eid": "1231231234",
	      "sourceCreatedDt": today,
	      "sourceModifiedDt": today,
	      "isDeleted": 'false'
	    }
	  ]
	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateCoreUser", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/IncomingDataRollsDownhillController/UpdateEid
	# Updates the Endpoints data based on a list of eids, crmIds and Core userIds, or inserts them as new endpoints if they don't already exist. 
	# Queue and Task items are created based upon what is inserted, deleted or updated.
	myJson = [
  		{
		    "coreUserId": 0,
		    "crmId": 1,
		    "eid": "1234561234",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today,
		    "isDeleted": 'false'
    	}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEid", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/IncomingDataRollsDownhillController/UpdateEntityLocationType
	# Updates the EntityLocationType data based on a list of entity location objects from Core Internal Services.
	myJson = [
  		{
		    "crmId": 0,
		    "coreUserId": 0,
		    "phoneId": 0,
		    "phoneNumbers": [
		      "string"
    ],
		    "locationValue": "string",
		    "locationCreatedDt": today,
		    "locationModifiedDt": today
    	}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEntityLocationType", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/IncomingDataRollsDownhillController/ProcessServiceBus
	# Processes all the data from the service bus and call the necessary APIs to update the data.
	myJson = {
	  "crmId": 1,
	  "complianceType": "Individual",
	  "companyClassification": None,
	  "isActive": 'true',
	  "person": {
	    "salutation": None,
	    "firstName": "asdf",
	    "lastName": "asdf",
	    "middleName": None,
	    "suffix": None,
	    "dateOfBirth": today,
	    "ssn": "1234",
	    "tin": None,
	    "hasNoSsnOrTin": 'true',
	    "companyCrmId": 0,
	    "modifiedDate": today,
	    "sourceCreatedDt": today,
	    "parentComplianceType": 0,
	    "parentCompanyClassification": 0,
	    "parentIsActive": 'true'
	  },
	  "company": None,
	  "address": {
	    "address1": "asdfasdf",
	    "address2": "asdf",
	    "city": "asdf",
	    "state": "asdf",
	    "postCode": "12345",
	    "country": "USA",
	    "modifiedDate": today,
	    "sourceCreatedDt": today
	  },
	  "documents": [
	    {
	      "documentId": "asdf",
	      "documentType": "asdf",
	      "documentFileLocation": "asdfasdf",
	      "documentModifiedDate": today,
	      "sourceCreatedDt": today
	    }
	  ],
	  "porting": [],
	  "guardians": []
	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ProcessServiceBus", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IncomingDataRollsDownhillController/ServiceBusMessageFailed
	# Records a failed service bus message, which will appear on the Failed Messages page
	myJson = {
	  "id": 0,
	  "crmId": 1,
	  "failureReason": "Test Failure",
	  "sequenceNumber": 0,
	  "messageId": "bf78d7b73715491f828712341231f123f",
	  "enqueuedTimeUtc": today,
	  "isFixed": 'true'
  	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ServiceBusMessageFailed", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed
	# Records a processed service bus message
	myJson = {
	  "id": 0,
	  "crmId": 1,
	  "messageBody": "This is a test",
	  "sequenceNumber": 979645,
	  "enqueuedTimeUtc": today
  	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IncomingDataRollsDownhillController/UpdateLastActivity
	# 
	myJson = [
  		{
		    "tdn": "1231231234",
		    "lastActivityDt": today
    	}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateLastActivity", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat
	# 
	myJson = [
  		{
		    "tdn": "1231231234",
		    "firstHeartbeatDt": today
    	}
	]
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)


def intelligence():
	# API Call for /api/IntelligenceController/ProcessAllIntelligence
	# Processes intelligence checks against the submission queue and account.
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessAllIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# /api/IntelligenceController/ProcessSubmissionQueueIntelligence
	# Processes intelligence checks against the submission queue to ensure our queue isn't getting clogged.
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api//api/IntelligenceController/ProcessSubmissionQueueIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IntelligenceController/ProcessAccountIntelligence
	# Processes intelligence checks against the account info to ensure we have all needed information and tasks are generated properly.
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessAccountIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IntelligenceController/ProcessTaskIntelligence
	# Processes intelligence checks against the task table to ensure the tasks are correct.
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessTaskIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
		
	# API Call for /api/IntelligenceController/ProcessPortIntelligence
	# Processes intelligence checks against port dates and the ACQ to ensure we are porting properly.
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessPortIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/IntelligenceController/ProcessEndpointIntelligence
	# Processes intelligence runs all intelligence checks against the wfl_Endpoint table.
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessEndpointIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)


def logging():
	# API Call for /api/LoggingController/LogException
	# Primary exception log handler integrated with splunk.
	myJson = {
	  "exception": "string",
	  "message": "string"
	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/LoggingController/LogException", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)
	
	# API Call for /api/LoggingController/LogInfoMessage
	# Primary Info log handler integrated with splunk.
	myJson = {
	  "exception": "string",
	  "message": "string"
	}
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/LoggingController/LogInfoMessage", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
		print(response.headers)
	except (ValueError):
		print("No Response Json")
		print(response.headers)


def readWorkflowController():
	# API Call for ReadWorkFlow/RetrieveTaskSummary
	response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveTaskSummary", auth=HttpNtlmAuth(username, password))
	print(response)
	print(response.json())

