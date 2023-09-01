import requests
import random
from requests_ntlm import HttpNtlmAuth
from datetime import date
from SQL_Functions import sql_Query, sql_Transaction
from lowercase_booleans import true
from FileCreateWrite import writeOutTestResults
from win32com.test.testPersist import now

# Authentication Credentials for API Call                
username = 'z_URDQA_Test'
password = '0irfI8El3E$)IXGX2jw9BIwlMo8^ql'

# Class Accessible Variables
today = date.today().strftime("%Y-%m-%d")
path = 'C:/TestResults/Test Automation Results.csv'
now = (str(date.today()) + " " + now.strftime("%H:%M:%S"))


def core_SyncControllerApiCalls():
	# API Call for /api/CoreSyncController/InsertEids
	# Takes a list of PhoneNumber and inserts those tdns into the wfl_Endpoint table and creates queue items where necessary.
	deleteTransaction = "use URD begin transaction delete from dat_RegisteredAddress where Endpoint_Id in (select Id from wfl_Endpoint where CrmId = 123123) commit transaction"
	sql_Transaction(deleteTransaction)
	deleteTransaction = "use URD begin transaction delete from wfl_Endpoint where CrmId = 123123 commit transaction"
	sql_Transaction(deleteTransaction)
	myJson = [
	  	{
		    "id": 0,
		    "crmId": 123123,
		    "eid": "1234567890",
		    "rdId": "123456789",
		    "lastActivityDt": today,
		    "firstHeartbeatDt": today,
		    "registrationDt": today,
		    "isMarkedForDelete": true,
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today
	  	}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/InsertEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select a.CrmId, a.Eid, a.RdId, CONVERT(VARCHAR(10), a.LastActivityDt, 120), CONVERT(VARCHAR(10), a.FirstHeartbeatDt, 120), CONVERT(VARCHAR(10), a.RegistrationDt, 120), a.IsMarkedForDelete, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from wfl_endpoint a where a.CrmId = 123123 and a.Eid = '1234567890'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(123123)
		jsonList.append("1234567890")
		jsonList.append("123456789")
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(True)
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			print(list1)
			print(sqlResult)
			writeOutTestResults(path, "/api/CoreSyncController/InsertEids", now, "Passed")
		else:
			print(list1)
			print(sqlResult)
			writeOutTestResults(path, "/api/CoreSyncController/InsertEids", now, "Failed")
	except (ValueError):
		print("No Response Status Code")
	
	# API Call for /api/CoreSyncController/DeleteEids
	# Takes a list of tdns and deletes those tdns from the wfl_Endpoint table or creates a terminate queue item.
	randomTDN = sql_Query("select top 1 a.Eid from wfl_Endpoint a where a.RdId is not null order by a.ModifiedDt")
	myJson = [
	  ' '.join(randomTDN[0])
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/DeleteEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select b.SubmissionQueueType_Id, b.SubmissionQueueStatus_Id, b.SubmissionQueueReason_Id, a.Eid, CONVERT(VARCHAR(10), b.CreatedDt, 120), CONVERT(VARCHAR(10), b.ModifiedDt, 120) from wfl_endpoint a join wfl_SubmissionQueue b on a.Id = b.Endpoint_Id where a.Eid = '" + ''.join(randomTDN[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(3)
		jsonList.append(3)
		jsonList.append(1)
		jsonList.append(' '.join(randomTDN[0]))
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			print(list1)
			print(sqlResult)
			writeOutTestResults(path, "/api/CoreSyncController/DeleteEids", now, "Passed")
		else:
			print(list1)
			print(sqlResult)
			writeOutTestResults(path, "/api/CoreSyncController/DeleteEids", now, "Failed")
	except (ValueError):
		print("No Response Status Code")
	
	# API Call for /api/CoreSyncController/UpdateEids
	# Takes a list of CrmEidCombo and updates the crmId in the wfl_Endpoint table and generates queue items where necessary.
	myJson = [
  		{
    		"eid": "2012040857",
     		"crmId": 123123
  		}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/UpdateEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select a.CrmId, a.Eid, b.SubmissionQueueType_Id, b.SubmissionQueueStatus_Id, b.SubmissionQueueReason_Id, b.RDID, b.CrmId, CONVERT(VARCHAR(10), b.CreatedDt, 120), CONVERT(VARCHAR(10), b.ModifiedDt, 120) from wfl_endpoint a join wfl_SubmissionQueue b on a.Id = b.Endpoint_Id where a.CrmId = 123123 and a.Eid = '2012040857'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(123123)
		jsonList.append("2012040857")
		jsonList.append(3)
		jsonList.append(3)
		jsonList.append(12)
		jsonList.append("107608184")
		jsonList.append(209338)
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			print(list1)
			print(sqlResult)
			writeOutTestResults(path, "/api/CoreSyncController/UpdateEids", now, "Passed")
		else:
			print(list1)
			print(sqlResult)
			writeOutTestResults(path, "/api/CoreSyncController/UpdateEids", now, "Failed")
	except (ValueError):
		print("No Response Status Code")
	
	# API Call for /api/CoreSyncController/InsertEmergencyAddresses
	# Takes a list of CrmEidCombo and updates the crmId in the wfl_Endpoint table and generates queue items where necessary.
	myJson = [
  		{
		    "eid": "7072666735",
		    "streetAddress": "4321 URD Street",
		    "streetAddressAdditionalInformation": "APT 1",
		    "city": "Nowhere",
		    "stateCode": "UT",
		    "zip5": "84000",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today
	    }
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/InsertEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select b.Eid, a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.CrmId = 172094 and b.Eid = '7072666735'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append("7072666735")
		jsonList.append("4321 URD Street")
		jsonList.append("APT 1")
		jsonList.append("Nowhere")
		jsonList.append("UT")
		jsonList.append("84000")
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/CoreSyncController/InsertEmergencyAddresses", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/CoreSyncController/InsertEmergencyAddresses", now, "Failed")
			print(list1)
			print(sqlResult)
	
	except (ValueError):
		print("No Response Status Code")

	# API Call for /api/CoreSyncController/UpdateEmergencyAddresses
	# Takes a list of CoreSyncEmergnecyAddresses and will update records in the dat_RegisteredAddress table.
	myJson = [
		{
		    "eid": "2012040857",
		    "streetAddress": "1234 URD Street",
		    "streetAddressAdditionalInformation": "APT 2",
		    "city": "Somewhere",
		    "stateCode": "UT",
		    "zip5": "84001",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today
		}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/UpdateEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select b.Eid, a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.CrmId = 123123 and b.Eid = '2012040857'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append("2012040857")
		jsonList.append("1234 URD Street")
		jsonList.append("APT 2")
		jsonList.append("Somewhere")
		jsonList.append("UT")
		jsonList.append("84001")
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/CoreSyncController/UpdateEmergencyAddresses", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/CoreSyncController/UpdateEmergencyAddresses", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Status Code")
	
	# API Call for /api/CoreSyncController/DeleteEmergencyAddresses
	# Takes a list of Eids and will remove records from the dat_RegisteredAddress table.
	myJson = [
			"2012040857"
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/DeleteEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select b.Eid, a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.CrmId = 123123 and b.Eid = '2012040857'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append("2012040857")
		jsonList.append(None)
		jsonList.append(None)
		jsonList.append(None)
		jsonList.append(None)
		jsonList.append(None)
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/CoreSyncController/DeleteEmergencyAddresses", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/CoreSyncController/DeleteEmergencyAddresses", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Status Code")
		
	# API Call for /api/CoreSyncController/InsertCoreAgreements
	# Inserts All new Core User Agreements
	# initializing list
	deleteTransaction = "use URD begin transaction delete from dat_UserAgreement where CrmId = 123123 commit transaction"
	sql_Transaction(deleteTransaction)
	numlist = [-1, 1, 9, 10, 13, 14, 15, 17]
	randomNum = random.choice(numlist)
	num = randomNum
	myJson = [
		{
		    "id": 0,
		    "crmId": 123123,
		    "agreement_Id": num,
		    "oldestAgreementDt": today,
		    "createdDt": today,
		    "sourceCreatedDt": today,
		    "modifiedDt": today,
		    "sourceModifiedDt": today
		}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/InsertCoreAgreements", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select a.CrmId, a.Agreement_Id, CONVERT(VARCHAR(10), a.OldestAgreementDt, 120), CONVERT(VARCHAR(10), a.CreatedDt, 120), CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.ModifiedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_UserAgreement a where a.CrmId = 123123"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(123123)
		jsonList.append(num)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/CoreSyncController/InsertCoreAgreements", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/CoreSyncController/InsertCoreAgreements", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Status Code")


def incomingDataRollsDownhill():
	# API Call for /api/IncomingDataRollsDownhillController/UpdateUrdAgreements
	# Update the user agreements in dat_UserDocument and set the Consent and SelfCert dates in dat_Person if they don't exist.
	deleteTransaction = "use URD begin transaction delete from dat_UserAgreement where CrmId = 123123 commit transaction"
	sql_Transaction(deleteTransaction)
	numlist = [-1, 1, 9, 10, 13, 14, 15, 17]
	randomNum = random.choice(numlist)
	num = randomNum
	myJson = {
	  "crmId": 123123,
	  "coreUserId": 0,
	  "consentAgreement_Id": num,
	  "consentCreatedDt": today,
	  "consentModifiedDt": today,
	  "selfCertificationAgreement_Id": num,
	  "selfCertificationCreatedDt": today,
	  "selfCertificationModifiedDt": today
	}
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateUrdAgreements", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select a.CrmId, a.Agreement_Id, CONVERT(VARCHAR(10), a.OldestAgreementDt, 120), CONVERT(VARCHAR(10), a.CreatedDt, 120), CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.ModifiedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_UserAgreement a where a.CrmId = 123123"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(123123)
		jsonList.append(num)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		jsonList.append(today)
		list1.append(jsonList)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateUrdAgreements", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateUrdAgreements", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Status Code")
	
	"""
	# API Call for /api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId
	# CoreUserHasNullCrmId will create an Endpoint with the Eid if it doesn't exist and a CrmId task if it doesn't exist.
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId?Eid=1234567890&CoreUserId=0", auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")

	# API Call for /api/IncomingDataRollsDownhillController/UpdateEmergencyAddress
	# UpdateEmergencyAddress will insert, delete or update an Emergency address to match the data passed into the method.
	myJson = {
	  "eids": [
	    "1234567890"
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
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEmergencyAddress", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")

	# API Call for /api/IncomingDataRollsDownhillController/UpdateCoreUser
	# Updates the Endpoints Crm information based on a list of eids, or inserts them as new endpoints if they don't already exist. 
	# Queue and Task items are created based upon what is inserted, deleted or updated.
	myJson = {
	  "coreUserId": 0,
	  "crmId": 123123,
	  "eids": [
	    {
	      "coreUserId": 0,
	      "crmId": 123123,
	      "eid": "1234567890",
	      "sourceCreatedDt": today,
	      "sourceModifiedDt": today,
	      "isDeleted": 'false'
	    }
	  ]
	}
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateCoreUser", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
		
	# API Call for /api/IncomingDataRollsDownhillController/UpdateEid
	# Updates the Endpoints data based on a list of eids, crmIds and Core userIds, or inserts them as new endpoints if they don't already exist. 
	# Queue and Task items are created based upon what is inserted, deleted or updated.
	myJson = [
  		{
		    "coreUserId": 0,
		    "crmId": 123123,
		    "eid": "1234567890",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today,
		    "isDeleted": 'false'
    	}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEid", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
		
	# API Call for /api/IncomingDataRollsDownhillController/UpdateEntityLocationType
	# Updates the EntityLocationType data based on a list of entity location objects from Core Internal Services.
	myJson = [
  		{
		    "crmId": 123123,
		    "coreUserId": 0,
		    "phoneId": 1,
		    "phoneNumbers": [
		      "1234567890"
    ],
		    "locationValue": "2",
		    "locationCreatedDt": today,
		    "locationModifiedDt": today
    	}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEntityLocationType", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
		
	# API Call for /api/IncomingDataRollsDownhillController/ProcessServiceBus
	# Processes all the data from the service bus and call the necessary APIs to update the data.
	myJson = {
	  "crmId": 123123,
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
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ProcessServiceBus", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
	
	# API Call for /api/IncomingDataRollsDownhillController/ServiceBusMessageFailed
	# Records a failed service bus message, which will appear on the Failed Messages page
	myJson = {
	  "id": 0,
	  "crmId": 123123,
	  "failureReason": "Test Failure",
	  "sequenceNumber": 0,
	  "messageId": "bf78d7b73715491f828712341231f123f",
	  "enqueuedTimeUtc": today,
	  "isFixed": 'true'
  	}
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ServiceBusMessageFailed", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
		
	# API Call for /api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed
	# Records a processed service bus message
	myJson = {
	  "id": 0,
	  "crmId": 123123,
	  "messageBody": "This is a test",
	  "sequenceNumber": 979645,
	  "enqueuedTimeUtc": today
  	}
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
	
	# API Call for /api/IncomingDataRollsDownhillController/UpdateLastActivity
	myJson = [
  		{
		    "tdn": "1234567890",
		    "lastActivityDt": today
    	}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateLastActivity", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
	
	# API Call for /api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat
	myJson = [
  		{
		    "tdn": "1234567890",
		    "firstHeartbeatDt": today
    	}
	]
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat", json=myJson, auth=HttpNtlmAuth(username, password))
		print("UpdateUrdAgreements")
		print(response)
		print(response.json())
	except (ValueError):
		print("UpdateUrdAgreements")
		print("No Response Json")
	"""


def intelligence():
	
	# /api/IntelligenceController/ProcessSubmissionQueueIntelligence
	# Processes intelligence checks against the submission queue to ensure our queue isn't getting clogged.
	# Try/Except Request and Process Response
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api//api/IntelligenceController/ProcessSubmissionQueueIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
	
	# API Call for /api/IntelligenceController/ProcessAccountIntelligence
	# Processes intelligence checks against the account info to ensure we have all needed information and tasks are generated properly.
	# Try/Except Request and Process Response
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessAccountIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
	
	# API Call for /api/IntelligenceController/ProcessTaskIntelligence
	# Processes intelligence checks against the task table to ensure the tasks are correct.
	# Try/Except Request and Process Response
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessTaskIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
		
	# API Call for /api/IntelligenceController/ProcessPortIntelligence
	# Processes intelligence checks against port dates and the ACQ to ensure we are porting properly.
	# Try/Except Request and Process Response
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessPortIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
	
	# API Call for /api/IntelligenceController/ProcessEndpointIntelligence
	# Processes intelligence runs all intelligence checks against the wfl_Endpoint table.
	# Try/Except Request and Process Response
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessEndpointIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
	"""
	# API Call for /api/IntelligenceController/ProcessAllIntelligence
	# Processes intelligence checks against the submission queue and account.
	# Try/Except Request and Process Response
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/IntelligenceController/ProcessAllIntelligence", auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
	"""


def logging():
	# API Call for /api/LoggingController/LogException
	# Primary exception log handler integrated with splunk.
	myJson = {
	  "exception": "string",
	  "message": "string"
	}
	# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/LoggingController/LogException", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response)
		print(response.json())
	except (ValueError):
		print("No Response Json")
	
	# API Call for /api/LoggingController/LogInfoMessage
	# Primary Info log handler integrated with splunk.
	myJson = {
	  "exception": "string",
	  "message": "string"
	}
	# Try/Except Request and Process Response
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

