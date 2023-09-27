import requests
import random
from requests_ntlm import HttpNtlmAuth
from datetime import date
from SQL_Functions import sql_Query, sql_Transaction, sql_QueryJsonResults, sql_QueryJsonResults2
from lowercase_booleans import true, false
from FileCreateWrite import writeOutTestResults
from win32com.test.testPersist import now
import json
from datetime import date
from _datetime import datetime
		
# Authentication Credentials for API Call                
username = 'z_URDQA_Test'
password = '0irfI8El3E$)IXGX2jw9BIwlMo8^ql'
		
# Class Accessible Variables
today = date.today().strftime("%Y-%m-%d")
path = 'C:/TestResults/Test Automation Results.csv'
now = (str(date.today()) + " " + now.strftime("%H:%M:%S"))
randomTDN = sql_Query("select top 1 a.Eid from wfl_Endpoint a where a.RdId is not null order by a.ModifiedDt")
randomTDN1 = sql_Query("select a.Eid from wfl_endpoint a where a.Id not in (select Endpoint_Id from dat_RegisteredAddress)")		

		
def core_SyncControllerApiCalls():
# API Call for /api/CoreSyncController/InsertEids
# Takes a list of PhoneNumber and inserts those tdns into the wfl_Endpoint table and creates queue items where necessary.
	deleteTransaction = "use URD begin transaction delete from wfl_Endpoint where CrmId = 100 commit transaction"
	sql_Transaction(deleteTransaction)
	myJson = [
	{
		"id": 0,
		"crmId": 100,
		"eid": "1234123400",
		"rdId": "123412340",
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
		query = "select a.CrmId, a.Eid, a.RdId, CONVERT(VARCHAR(10), a.LastActivityDt, 120), CONVERT(VARCHAR(10), a.FirstHeartbeatDt, 120), CONVERT(VARCHAR(10), a.RegistrationDt, 120), a.IsMarkedForDelete, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from wfl_endpoint a where a.CrmId = 100 and a.Eid = '1234123400'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(100)
		jsonList.append("1234123400")
		jsonList.append("123412340")
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
		"eid": ' '.join(randomTDN[0]),
		"crmId": 123456
	}
]
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/UpdateEids", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select a.CrmId, a.Eid, CONVERT(VARCHAR(10), b.CreatedDt, 120), CONVERT(VARCHAR(10), b.ModifiedDt, 120) from wfl_endpoint a join wfl_SubmissionQueue b on a.Id = b.Endpoint_Id where a.CrmId = 123456 and a.Eid =  '" + ' '.join(randomTDN[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(123456)
		jsonList.append(' '.join(randomTDN[0]))
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
# Takes a list of CoreSyncEmergnecyAddresses and will create new records in the dat_RegisteredAddress table.
	myJson = [
	{
		"eid": ' '.join(randomTDN1[0]),
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
		query = "select b.Eid, a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.Eid = '" + ' '.join(randomTDN1[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(' '.join(randomTDN1[0]))
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
		    "eid": ' '.join(randomTDN1[0]),
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
		query = "select b.Eid, a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.Eid = '" + ' '.join(randomTDN1[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(' '.join(randomTDN1[0]))
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
		 ' '.join(randomTDN1[0])
	]
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/CoreSyncController/DeleteEmergencyAddresses", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select b.Eid, a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.Eid = '" + ' '.join(randomTDN1[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(' '.join(randomTDN1[0]))
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
	deleteTransaction = "use URD begin transaction delete from dat_UserAgreement where CrmId = 123456 commit transaction"
	sql_Transaction(deleteTransaction)
	numlist = [-1, 1, 9, 10, 13, 14, 15, 17]
	randomNum = random.choice(numlist)
	num = randomNum
	myJson = [
		{
		    "id": 0,
		    "crmId": 123456,
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
		query = "select a.CrmId, a.Agreement_Id, CONVERT(VARCHAR(10), a.OldestAgreementDt, 120), CONVERT(VARCHAR(10), a.CreatedDt, 120), CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.ModifiedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_UserAgreement a where a.CrmId = 123456"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList = []
		jsonList.append(123456)
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
	deleteTransaction = "use URD begin transaction delete from dat_UserAgreement where CrmId = 123456 commit transaction"
	sql_Transaction(deleteTransaction)
	numlist = [-1, 1, 9, 10, 13, 14, 15, 17]
	randomNum1 = random.choice(numlist)
	randomNum2 = random.choice(numlist)
	myJson = {
		 "crmId": 123456,
		 "coreUserId": 0,
		 "consentAgreement_Id": randomNum1,
		 "consentCreatedDt": today,
		 "consentModifiedDt": today,
		 "selfCertificationAgreement_Id": randomNum2,
		 "selfCertificationCreatedDt": today,
		 "selfCertificationModifiedDt": today
		}
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateUrdAgreements", json=myJson, auth=HttpNtlmAuth(username, password))
		print(response.status_code)
		query = "select a.CrmId, a.Agreement_Id, CONVERT(VARCHAR(10), a.OldestAgreementDt, 120), CONVERT(VARCHAR(10), a.CreatedDt, 120), CONVERT(VARCHAR(10), a.SourceCreatedDt, 120), CONVERT(VARCHAR(10), a.ModifiedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_UserAgreement a where a.CrmId = 123456"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(123456)
		jsonList1.append(randomNum1)
		jsonList1.append(today)
		jsonList1.append(today)
		jsonList1.append(today)
		jsonList1.append(today)
		jsonList1.append(today)
		list1.append(jsonList1)
		jsonList2 = []
		jsonList2.append(123456)
		jsonList2.append(randomNum2)
		jsonList2.append(today)
		jsonList2.append(today)
		jsonList2.append(today)
		jsonList2.append(today)
		jsonList2.append(today)
		list1.append(jsonList2)
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
		
# API Call for /api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId
# CoreUserHasNullCrmId will create an Endpoint with the Eid if it doesn't exist and a CrmId task if it doesn't exist.
	deleteTransaction = "use URD begin transaction delete from wfl_Endpoint where Eid = '9876543210' commit transaction"
	sql_Transaction(deleteTransaction)
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId?Eid=9876543210&CoreUserId=0", auth=HttpNtlmAuth(username, password))
		query = "select a.CrmId, a.Eid, CONVERT(VARCHAR(10), a.CreatedDt, 120) from wfl_Endpoint a where a.Eid = '9876543210'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(-1)
		jsonList1.append('9876543210')
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/CoreUserHasNullCrmId", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/UpdateEmergencyAddress
# UpdateEmergencyAddress will insert, delete or update an Emergency address to match the data passed into the method.
	deleteTransaction = "use URD begin transaction delete from dat_RegisteredAddress where Endpoint_Id in (select Id from wfl_Endpoint where Eid = '9876543210') commit transaction"
	sql_Transaction(deleteTransaction)
	myJson = {
		 "eids": [
		   "9876543210"
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
		query = "select a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.CreatedDt, 120), CONVERT(VARCHAR(10), a.SourceModifiedDt, 120) from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.Eid = '9876543210'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append("1234 Testing Street")
		jsonList1.append("APT 1")
		jsonList1.append("Nowhere")
		jsonList1.append("UT")
		jsonList1.append("84000")
		jsonList1.append(today)
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateEmergencyAddress", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateEmergencyAddress", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/UpdateCoreUser
# Updates the Endpoints Crm information based on a list of eids, or inserts them as new endpoints if they don't already exist. 
# Queue and Task items are created based upon what is inserted, deleted or updated.
	deleteTransaction = "use URD begin transaction delete from wfl_Endpoint where Eid = '9999999999' commit transaction"
	sql_Transaction(deleteTransaction)
	myJson = {
		 "coreUserId": 0,
		 "crmId": 123123,
		 "eids": [
		   {
		     "coreUserId": 0,
		     "crmId": 123123,
		     "eid": "9999999999",
		     "sourceCreatedDt": today,
		     "sourceModifiedDt": today,
		     "isDeleted": 'false'
		   }
		 ]
	}
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateCoreUser", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.CrmId, a.Eid, CONVERT(VARCHAR(10), a.CreatedDt, 120) from wfl_Endpoint a where a.Eid = '9999999999'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(123123)
		jsonList1.append('9999999999')
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateCoreUser", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateCoreUser", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/UpdateEid
# Updates the Endpoints data based on a list of eids, crmIds and Core userIds, or inserts them as new endpoints if they don't already exist. 
# Queue and Task items are created based upon what is inserted, deleted or updated.
	deleteTransaction = "use URD begin transaction delete from wfl_Endpoint where Eid = '1111111111' commit transaction"
	sql_Transaction(deleteTransaction)
	myJson = [
		  {
		    "coreUserId": 0,
		    "crmId": 123123,
		    "eid": "1111111111",
		    "sourceCreatedDt": today,
		    "sourceModifiedDt": today,
		    "isDeleted": 'false'
		   }
	]
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEid", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.CrmId, a.Eid, CONVERT(VARCHAR(10), a.CreatedDt, 120) from wfl_Endpoint a where a.Eid = '1111111111'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(123123)
		jsonList1.append('1111111111')
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateEid", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateEid", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/UpdateEntityLocationType
# Updates the EntityLocationType data based on a list of entity location objects from Core Internal Services.
	numlist = [-1 , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7]
	randomNum1 = random.choice(numlist)
	myJson = [
		  {
		    "crmId":123123,
		    "coreUserId": 0,
		    "phoneId": 1,
		    "phoneNumbers": [
		      "11111111111"
		  ],
		    "locationValue": randomNum1,
		    "locationCreatedDt": today,
		    "locationModifiedDt": today
		   }
	]
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateEntityLocationType", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select b.CrmId, b.Eid, CONVERT(VARCHAR(10), a.ModifiedDt, 120), a.EntityLocationType_Id from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id where b.Eid = '1111111111'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(123123)
		jsonList1.append('1111111111')
		jsonList1.append(today)
		jsonList1.append(randomNum1)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateEntityLocationType", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateEntityLocationType", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/ProcessServiceBus
# Processes all the data from the service bus and call the necessary APIs to update the data.
	myJson = {
		 "crmId": 7908,
		 "complianceType": "Individual",
		 "companyClassification": None,
		 "isActive": 'true',
		 "person": {
		   "salutation": None,
		   "firstName": "Test",
		   "lastName": "Test",
		   "middleName": None,
		   "suffix": None,
		   "dateOfBirth": "1950-01-1",
		   "ssn": "1234",
		   "tin": None,
		   "hasNoSsnOrTin": 'true',
		   "companyCrmId": 0,
		   "modifiedDate": "2023-09-13",
		   "sourceCreatedDt": "2023-09-13",
		   "parentComplianceType": 0,
		   "parentCompanyClassification": 0,
		   "parentIsActive": 'true'
		 },
		 "company": None,
		 "address": {
		   "address1": "Testing Street",
		   "address2": "Test",
		   "city": "Test",
		   "state": "Testing",
		   "postCode": "12345",
		   "country": "USA",
		   "modifiedDate": "2023-09-13",
		   "sourceCreatedDt": "2023-09-13"
		 },
		 "documents": [
		   {
		     "documentId": "10651032-122a-4f02-8c4a-4b4cfdbc2264",
		     "documentType": "SO3PI",
		     "documentFileLocation": "https://indeocorp.sharepoint.com/sites/VRSProdDynamicsDocs/account/Darrell%20Duncan_EEA830C75C484132B477A9E062D90494/76BDCDA6-5E56-44F3-8F29-ADC6F6B3BDAB.docx",
		     "documentModifiedDate": "2023-09-13",
		     "sourceCreatedDt": "2023-09-13"
		   }
		 ],
		 "porting": [],
		 "guardians": []
	}
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ProcessServiceBus", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.StreetAddress, a.StreetAddressAdditionalInformation, a.City, a.StateCode, a.Zip5, CONVERT(VARCHAR(10), a.ModifiedDt, 120), b.ComplianceType_Id, b.FirstName, b.LastName, b.Last4SSN, b.DOB, CONVERT(VARCHAR(10), b.ModifiedDt, 120), c.DocumentId, c.FileLocation from dat_ResidentialAddress a join dat_Person b on a.CrmId = b.CrmId join dat_UserDocument c on a.CrmId = c.CrmId where b.ComplianceType_Id = 581 and a.CrmId = 7908"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append("Testing Street")
		jsonList1.append("Test")
		jsonList1.append("Test")
		jsonList1.append("Testing")
		jsonList1.append("12345")
		jsonList1.append(today)
		jsonList1.append(581)
		jsonList1.append("Test")
		jsonList1.append("Test")
		jsonList1.append("1234")
		jsonList1.append("1950-01-01")
		jsonList1.append(today)
		jsonList1.append("10651032-122a-4f02-8c4a-4b4cfdbc2264")
		jsonList1.append("https://indeocorp.sharepoint.com/sites/VRSProdDynamicsDocs/account/Darrell%20Duncan_EEA830C75C484132B477A9E062D90494/76BDCDA6-5E56-44F3-8F29-ADC6F6B3BDAB.docx")
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/ProcessServiceBus", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/ProcessServiceBus", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
		# API Call for /api/IncomingDataRollsDownhillController/ServiceBusMessageFailed
		# Records a failed service bus message, which will appear on the Failed Messages page
		deleteTransaction = "use URD begin transaction delete from sb_FailedMessages where MessageId = 'bf78d7b73715491f8287123412Testing' commit transaction"
		sql_Transaction(deleteTransaction)
		myJson = {
		 "id": 0,
		 "crmId": 123123,
		 "failureReason": "This is a test.",
		 "sequenceNumber": 0,
		 "messageId": "bf78d7b73715491f8287123412Testing",
		 "enqueuedTimeUtc": today,
		 "isFixed": 'true'
		 }
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ServiceBusMessageFailed", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.CrmId, a.FailureReason, a.MessageId, CONVERT(VARCHAR(10), a.CreatedDt, 120) from sb_FailedMessages a where a.MessageId = 'bf78d7b73715491f8287123412Testing'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(123123)
		jsonList1.append("This is a test.")
		jsonList1.append("bf78d7b73715491f8287123412Testing")
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/ServiceBusMessageFailed", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/ServiceBusMessageFailed", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed
# Records a processed service bus message
	deleteTransaction = "use URD begin transaction delete from sb_ProcessedMessages where SequenceNumber = 979645 commit transaction"
	sql_Transaction(deleteTransaction)
	myJson = {
		 "id": 0,
		 "crmId": 123123,
		 "messageBody": "This is a test.",
		 "sequenceNumber": 979645,
		 "enqueuedTimeUtc": today
	}
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.CrmId, a.MessageBody, a.SequenceNumber, CONVERT(VARCHAR(10), a.CreatedDt, 120) from sb_ProcessedMessages a where a.SequenceNumber = 979645"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(123123)
		jsonList1.append("This is a test.")
		jsonList1.append(979645)
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/ServiceBusMessageProcessed", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/UpdateLastActivity
	myJson = [
	{
		    "tdn": (' '.join(randomTDN[0])),
		    "lastActivityDt": today
		   }
	]
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateLastActivity", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.Eid, CONVERT(VARCHAR(10), a.LastActivityDt, 120) from wfl_Endpoint a where a.Eid =  '" + ' '.join(randomTDN[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(' '.join(randomTDN[0]))
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateLastActivity", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateLastActivity", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat
	myJson = [
		 {
		    "tdn": (' '.join(randomTDN[0])),
		    "firstHeartbeatDt": today
		   }
	]
# Try/Except Request and Process Response
	try:
		response = requests.post("http://urd-qa.corp.srelay.com/URA/api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat", json=myJson, auth=HttpNtlmAuth(username, password))
		query = "select a.Eid, CONVERT(VARCHAR(10), a.FirstHeartbeatDt,  120) from wfl_Endpoint a where a.Eid =  '" + ' '.join(randomTDN[0]) + "'"
		sqlResult = sql_Query(query)
		list1 = []
		jsonList1 = []
		jsonList1.append(' '.join(randomTDN[0]))
		jsonList1.append(today)
		list1.append(jsonList1)
		if (sqlResult == list1) and (response.status_code == 200):
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat", now, "Passed")
			print(list1)
			print(sqlResult)
		else:
			writeOutTestResults(path, "/api/IncomingDataRollsDownhillController/UpdateFirstHeartbeat", now, "Failed")
			print(list1)
			print(sqlResult)
	except (ValueError):
		print("No Response Json")

		
def readWorkflowController():
# API Call for /api/ReadWorkflowController/RetrieveTaskSummary
	try:
		query = "SELECT ft.Id as id,ft.TaskType as taskType,SUM(ft.NumCrm) [count] FROM (SELECT t.TaskType_Id [Id],tt.[Name] [TaskType],COUNT(DISTINCT e.CrmId) AS NumCrm FROM dbo.wfl_Task AS t JOIN dbo.wfl_Endpoint AS e ON t.Endpoint_Id = e.Id JOIN dbo.wfl_TaskType AS tt ON t.TaskType_Id = tt.Id GROUP BY t.TaskType_Id,tt.Name) ft GROUP BY ft.TaskType, ft.Id ORDER BY [Count] DESC"
		sqlResult = sql_QueryJsonResults(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveTaskSummary", auth=HttpNtlmAuth(username, password))
		result = any(elem in sqlResult for elem in response.json())
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskSummary", now, "Passed")
			print(response.json())
			print(sqlResult)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskSummary", now, "Failed")
			print(response.json())
			print(sqlResult)
			print(false)
	except (ValueError):
		print("No Response Json")
	
# API Call for /api/ReadWorkflowController/RetrieveSubmissionQueueSummary
	try:
		query = "SELECT SUM(CASE WHEN sq.SubmissionQueueType_Id = 1 THEN 1 ELSE 0 END) [new], SUM(CASE WHEN sq.SubmissionQueueType_Id = 2 THEN 1 ELSE 0 END) [update], SUM(CASE WHEN sq.SubmissionQueueType_Id = 3 THEN 1 ELSE 0 END) [terminate], SUM(CASE WHEN sq.SubmissionQueueType_Id = 4 THEN 1 ELSE 0 END) [transfer], SUM(CASE WHEN sq.SubmissionQueueType_Id = 5 THEN 1 ELSE 0 END) [abandon], SUM(CASE WHEN sq.SubmissionQueueType_Id = 6 THEN 1 ELSE 0 END) [port]  FROM dbo.wfl_SubmissionQueue sq"
		sqlResult = sql_QueryJsonResults(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveSubmissionQueueSummary", auth=HttpNtlmAuth(username, password))
		jsonList = []
		jsonList.append(response.json())
		result = any(elem in sqlResult for elem in jsonList)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveSubmissionQueueSummary", now, "Passed")
			print(jsonList)
			print(sqlResult)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveSubmissionQueueSummary", now, "Failed")
			print(jsonList)
			print(sqlResult)
			print(false)
	except (ValueError):
		print("No Response Json")
# API Call for /api/ReadWorkflowController/RetrieveRegistrationRecap
	try:
		query = "SELECT SUM(CASE WHEN p.Id IS NOT NULL AND e.RegistrationDt <= GETUTCDATE() THEN 1 ELSE 0 END) [today], SUM(CASE WHEN p.Id IS NOT NULL AND e.RegistrationDt <= (GETUTCDATE() - 7) THEN 1 ELSE 0 END) [oneWeekAgo], SUM(CASE WHEN p.Id IS NOT NULL AND e.RegistrationDt <= (GETUTCDATE() - 14) THEN 1 ELSE 0 END) [twoWeeksAgo], SUM(CASE WHEN p.Id IS NOT NULL AND e.RegistrationDt <= GETUTCDATE() THEN 1 ELSE 0 END) - SUM(CASE WHEN p.Id IS NOT NULL AND e.RegistrationDt <= (GETUTCDATE() - 14) THEN 1 ELSE 0 END) [change], SUM(CASE WHEN c.Id IS NOT NULL AND e.RegistrationDt <= GETUTCDATE() THEN 1 ELSE 0 END) [entityToday], SUM(CASE WHEN c.Id IS NOT NULL AND e.RegistrationDt <= (GETUTCDATE() - 7) THEN 1 ELSE 0 END) [entityOneWeekAgo], SUM(CASE WHEN c.Id IS NOT NULL AND e.RegistrationDt <= (GETUTCDATE() - 14) THEN 1 ELSE 0 END) [entityTwoWeeksAgo], SUM(CASE WHEN c.Id IS NOT NULL AND e.RegistrationDt <= GETUTCDATE() THEN 1 ELSE 0 END) - SUM(CASE WHEN c.Id IS NOT NULL AND e.RegistrationDt <= (GETUTCDATE() - 14) THEN 1 ELSE 0 END) [entityChange] FROM dbo.wfl_Endpoint e LEFT JOIN dbo.dat_Person p ON p.CrmId = e.CrmId LEFT JOIN dbo.dat_Company c ON c.CrmId = e.CrmId WHERE RdId > ''"
		sqlResult = sql_QueryJsonResults(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveRegistrationRecap", auth=HttpNtlmAuth(username, password))
		jsonList = []
		jsonList.append(response.json())
		result = any(elem in sqlResult for elem in jsonList)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveRegistrationRecap", now, "Passed")
			print(jsonList)
			print(sqlResult)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveRegistrationRecap", now, "Failed")
			print(jsonList)
			print(sqlResult)
			print(false)
	except (ValueError):
		print("No Response Json") 
# API Call for /api/ReadWorkflowController/RetrieveFullTaskList
	try:
		query = "SELECT tasks.Id, tasks.CrmId, tasks.Eid, ct.[Name] [ComplianceType], tasks.TaskType_Id, tasks.[TaskType], tasks.[ResultDescription], tasks.Notes, tasks.AuditNotes, tasks.FirstHeartbeatDt, tasks.NumberOfAttempts, tasks.CreatedDt, CASE WHEN ct.[Name] = 'Minor' AND a.DOB <= DATEADD(YEAR, -18, GETUTCDATE()) THEN CONVERT(BIT, 1) ELSE CONVERT(BIT, 0) END [IsMinorAnAdult], consent.OldestAgreementDt [ConsentDt], selfcert.OldestAgreementDt [SelfCertificationDt] FROM (SELECT * FROM (SELECT t.Id, e.CrmId, e.Eid, t.TaskType_Id, tt.[Name] [TaskType], t.[Description] [ResultDescription], t.Notes, t.AuditNotes, e.FirstHeartbeatDt, sq.NumberOfAttempts, t.CreatedDt, ROW_NUMBER() OVER (PARTITION BY e.CrmId, t.TaskType_Id ORDER BY t.CreatedDt ASC) rn FROM dbo.wfl_Endpoint e JOIN dbo.wfl_Task t ON t.Endpoint_Id = e.Id JOIN dbo.wfl_TaskType tt ON t.TaskType_Id = tt.Id LEFT JOIN dbo.wfl_SubmissionQueue sq on t.SubmissionQueue_Id = sq.Id) AS t WHERE t.rn = 1) tasks LEFT JOIN (SELECT p.CrmId, p.ComplianceType_Id, TRY_CAST(p.[DOB] AS DATETIME2(3)) AS DOB FROM dbo.dat_Person p UNION SELECT c.CrmId, c.ComplianceType_Id, NULL [DOB] FROM dbo.dat_Company c) a ON a.CrmId = tasks.CrmId LEFT JOIN dbo.dat_ComplianceType ct ON ct.Id = a.ComplianceType_Id OUTER APPLY (SELECT TOP 1 ua.OldestAgreementDt FROM dbo.dat_UserAgreement ua JOIN dbo.dat_Agreement a ON a.Id = ua.Agreement_Id AND a.AgreementType_Id = 1 WHERE ua.CrmId = tasks.CrmId ORDER BY ua.OldestAgreementDt ASC) consent OUTER APPLY (SELECT TOP 1 ua.OldestAgreementDt FROM dbo.dat_UserAgreement ua JOIN dbo.dat_Agreement a ON a.Id = ua.Agreement_Id AND a.AgreementType_Id = 4 WHERE ua.CrmId = tasks.CrmId ORDER BY ua.OldestAgreementDt ASC)selfcert"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveFullTaskList", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullTaskList", now, "Passed")
			print(responseCount)
			print(sqlCount)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullTaskList", now, "Failed")
			print(responseCount)
			print(sqlCount)
			print(false)
	except (ValueError):
		print("No Response Json")
	
# API Call for /api/ReadWorkflowController/RetrieveFullTaskListCSV
	try:
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveFullTaskListCSV", auth=HttpNtlmAuth(username, password))
		if (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullTaskListCSV", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullTaskListCSV", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")
# API Call for /api/ReadWorkflowController/RetrieveFullEidList
	try:
		query = "select a.Eid from wfl_Endpoint a"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveFullEidList", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullEidList", now, "Passed")
			print(responseCount)
			print(sqlCount)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullEidList", now, "Failed")
			print(responseCount)
			print(sqlCount)
			print(false)
	except (ValueError):
		print("No Response Json") 
# API Call for /api/ReadWorkflowController/RetrieveFullEidCrmList
	try:
		query = "SELECT e.Id, e.Eid, e.CrmId, ch.RootCrmId [RootCrmId], CASE WHEN tasks.OutstandingTasks IS NULL THEN 0 ELSE tasks.OutstandingTasks END [Tasks], CASE WHEN queueItems.SubmissionQueueItems IS NULL THEN 0 ELSE queueItems.SubmissionQueueItems END [QueueItems], e.FirstHeartbeatDt, e.LastActivityDt, e.RdId FROM dbo.wfl_Endpoint e LEFT JOIN dbo.v_CompanyHierarchy ch ON ch.CrmId = e.CrmId OUTER APPLY (SELECT COUNT(ft.Id) [OutstandingTasks] FROM (SELECT t.Id ,ROW_NUMBER() OVER (PARTITION BY e2.CrmId, tt.[Name] ORDER BY t.CreatedDt ASC) rn FROM dbo.wfl_Task t JOIN dbo.wfl_Endpoint e2 ON e2.Id = t.Endpoint_Id JOIN dbo.wfl_TaskType tt ON t.TaskType_Id = tt.Id WHERE t.Endpoint_Id = e.Id) ft WHERE rn = 1) tasks OUTER APPLY (SELECT COUNT(sq.Id) [SubmissionQueueItems] FROM dbo.wfl_SubmissionQueue sq JOIN dbo.wfl_Endpoint ie ON sq.Endpoint_Id = ie.Id WHERE sq.Endpoint_Id = e.Id) queueItems"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveFullEidCrmList", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullEidCrmList", now, "Passed")
			print(responseCount)
			print(sqlCount)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullEidCrmList", now, "Failed")
			print(responseCount)
			print(sqlCount)
			print(false)
	except (ValueError):
		print("No Response Json")
# API Call for /api/ReadWorkflowController/RetrieveFullCrmList
	try:
		query = "SELECT  A.CrmId FROM (SELECT  CrmId FROM  dbo.dat_Person WHERE  IsActive = 1 UNION SELECT  CrmId FROM  dbo.dat_Company WHERE  IsActive = 1 UNION SELECT  CrmId FROM  dbo.wfl_Endpoint)AS A WHERE  A.CrmId > 0"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveFullCrmList", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullCrmList", now, "Passed")
			print(responseCount)
			print(sqlCount)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveFullCrmList", now, "Failed")
			print(responseCount)
			print(sqlCount)
			print(false)
	except (ValueError):
		print("No Response Json")
# API Call for /api/ReadWorkflowController/RetrieveResidentialAddresses
	try:
		query = "SELECT HistoryId as historyId, StreetAddress as streetAddress, StreetAddressAdditionalInformation as streetAddressAdditionalInformation, City as city, StateCode as stateCode, Zip5 as zip5 FROM (SELECT HistoryId, StreetAddress, StreetAddressAdditionalInformation, City, StateCode, Zip5, HistoryEndDt, ROW_NUMBER() OVER (PARTITION BY StreetAddress, StreetAddressAdditionalInformation, City, StateCode, Zip5 ORDER BY HistoryEndDt DESC) AS RowNo FROM (SELECT-1 [HistoryId], ISNULL(StreetAddress, '') AS StreetAddress, ISNULL(StreetAddressAdditionalInformation, '') AS StreetAddressAdditionalInformation, ISNULL(City, '') AS City, ISNULL(StateCode, '') AS StateCode, ISNULL(Zip5, '') AS Zip5, '12/31/9999' as HistoryEndDt FROM dbo.dat_ResidentialAddress WHERE CrmId in (SELECT TOP 1 e.CrmId FROM dbo.wfl_Task t JOIN dbo.wfl_Endpoint e ON t.Endpoint_Id = e.Id WHERE t.Id = 1) UNION SELECT HistoryId as historyId, ISNULL(StreetAddress, '') AS streetAddress, ISNULL(StreetAddressAdditionalInformation, '') AS streetAddressAdditionalInformation, ISNULL(City, '') AS city, ISNULL(StateCode, '') AS stateCode, ISNULL(Zip5, '') AS zip5, HistoryEndDt FROM dbo.dat_ResidentialAddressHistory WITH (NOLOCK) WHERE CrmId in (SELECT TOP 1 e.CrmId FROM dbo.wfl_Task t JOIN dbo.wfl_Endpoint e ON t.Endpoint_Id = e.Id WHERE t.Id = 1)AND (StreetAddress IS NOT NULL OR StreetAddressAdditionalInformation IS NOT NULL OR City IS NOT NULL OR StateCode IS NOT NULL OR Zip5 IS NOT NULL)) priority) t WHERE t.RowNo = 1 ORDER BY t.HistoryEndDt DESC"
		sqlResult = sql_QueryJsonResults(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveResidentialAddresses?task_Id=1", auth=HttpNtlmAuth(username, password))
		if (sqlResult == response.json()) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveResidentialAddresses", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveResidentialAddresses", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")
# API Call for /api/ReadWorkflowController/RetrieveNullHeartbeatEids
	try:
		query = "SELECT Eid FROM dbo.wfl_Endpoint WHERE FirstHeartbeatDt IS NULL"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveNullHeartbeatEids", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveNullHeartbeatEids", now, "Passed")
			print(responseCount)
			print(sqlCount)
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveNullHeartbeatEids", now, "Failed")
			print(responseCount)
			print(sqlCount)
			print(false)
	except (ValueError):
		print("No Response Json")
# API Call for /api/ReadWorkflowController/RetrieveIndividualTask
	try:
		query = "DECLARE @CrmId BIGINT = (SELECT TOP 1 e.CrmId FROM dbo.wfl_Task t JOIN dbo.wfl_Endpoint e ON e.Id = t.Endpoint_Id WHERE t.Id = 1)DECLARE @RootCrmId BIGINT = dbo.udfn_GetRootCrmId(@CrmId) DECLARE @IsNullRootCrmId BIGINT = ISNULL(@RootCrmId, @CrmId) SELECT TOP 1 e.CrmId,ISNULL(e.Eid,''),ISNULL(tt.[Name],'') [TaskType],ISNULL(t.[Description],'') [ResultDescription] FROM dbo.wfl_Endpoint e JOIN dbo.wfl_Task t ON t.Endpoint_Id = e.Id JOIN dbo.wfl_TaskType tt ON t.TaskType_Id = tt.Id  JOIN dbo.vdat_AllAccounts a ON a.CrmId = e.CrmId JOIN dbo.dat_ComplianceType ct ON ct.Id = a.ComplianceType_Id LEFT JOIN dbo.wfl_SubmissionQueue sq ON t.SubmissionQueue_Id = sq.Id LEFT JOIN dbo.wfl_TaskHistory th_n WITH (NOLOCK) ON t.Id = th_n.Id LEFT JOIN dbo.wfl_TaskHistory th_an WITH (NOLOCK) ON t.Id = th_an.Id LEFT JOIN dbo.dat_ResidentialAddress ra ON ra.CrmId = @IsNullRootCrmId LEFT JOIN dbo.dat_ResidentialAddressHistory rah WITH (NOLOCK) ON ra.PriorityHistoryId = rah.HistoryId LEFT JOIN dbo.dat_Company rootC ON rootC.CrmId = @IsNullRootCrmId LEFT JOIN dbo.dat_CompanyContact rootCC ON rootCC.Id = rootC.CompanyContact_Id OUTER APPLY (SELECT TOP 1 * FROM dbo.dat_ResidentialAddressHistory rah2 WITH (NOLOCK) WHERE rah2.CrmId = a.CrmId) addressHist OUTER APPLY (SELECT TOP 1 th.HistoryEndDt FROM dbo.wfl_TaskHistory th WITH (NOLOCK) WHERE th.Id = t.Id AND th.Notes IS NOT NULL AND th.Notes = t.Notes ORDER BY th.HistoryEndDt DESC) noteHist OUTER APPLY (SELECT TOP 1 th.HistoryEndDt FROM dbo.wfl_TaskHistory th WITH (NOLOCK) WHERE th.Id = t.Id AND th.AuditNotes IS NOT NULL AND th.AuditNotes = t.AuditNotes ORDER BY th.HistoryEndDt DESC) auditNoteHist WHERE t.Id = 1"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveIndividualTask?id=1", auth=HttpNtlmAuth(username, password))
		responseJson1 = []
		responseJson1.append(response.json()["crmId"])
		responseJson1.append(response.json()["eid"])
		responseJson1.append(response.json()["taskType"])
		responseJson1.append(response.json()["resultDescription"])
		responseJson2 = []
		responseJson2.append(responseJson1)
		result = any(elem in sqlResult for elem in responseJson2)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveIndividualTask", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveIndividualTask", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")
		
# API Call for /api/ReadWorkflowController/RetrieveTaskListCrmId
	try:
		crmIdValue = sql_Query("select top 1 b.CrmId from wfl_Task a join wfl_Endpoint b on a.Endpoint_Id = b.Id")
		query = "DECLARE @CrmId BIGINT = (SELECT TOP 1 e.CrmId FROM dbo.wfl_Task t JOIN dbo.wfl_Endpoint e ON e.Id = t.Endpoint_Id WHERE t.Id = 1)DECLARE @RootCrmId BIGINT = dbo.udfn_GetRootCrmId(@CrmId) DECLARE @IsNullRootCrmId BIGINT = ISNULL(@RootCrmId, @CrmId) SELECT TOP 1 t.Id, e.CrmId,ISNULL(e.Eid,''),ISNULL(tt.[Name],'') [TaskType],ISNULL(t.[Description],'') [ResultDescription] FROM dbo.wfl_Endpoint e JOIN dbo.wfl_Task t ON t.Endpoint_Id = e.Id JOIN dbo.wfl_TaskType tt ON t.TaskType_Id = tt.Id  JOIN dbo.vdat_AllAccounts a ON a.CrmId = e.CrmId JOIN dbo.dat_ComplianceType ct ON ct.Id = a.ComplianceType_Id LEFT JOIN dbo.wfl_SubmissionQueue sq ON t.SubmissionQueue_Id = sq.Id LEFT JOIN dbo.wfl_TaskHistory th_n WITH (NOLOCK) ON t.Id = th_n.Id LEFT JOIN dbo.wfl_TaskHistory th_an WITH (NOLOCK) ON t.Id = th_an.Id LEFT JOIN dbo.dat_ResidentialAddress ra ON ra.CrmId = @IsNullRootCrmId LEFT JOIN dbo.dat_ResidentialAddressHistory rah WITH (NOLOCK) ON ra.PriorityHistoryId = rah.HistoryId LEFT JOIN dbo.dat_Company rootC ON rootC.CrmId = @IsNullRootCrmId LEFT JOIN dbo.dat_CompanyContact rootCC ON rootCC.Id = rootC.CompanyContact_Id OUTER APPLY (SELECT TOP 1 * FROM dbo.dat_ResidentialAddressHistory rah2 WITH (NOLOCK) WHERE rah2.CrmId = a.CrmId) addressHist OUTER APPLY (SELECT TOP 1 th.HistoryEndDt FROM dbo.wfl_TaskHistory th WITH (NOLOCK) WHERE th.Id = t.Id AND th.Notes IS NOT NULL AND th.Notes = t.Notes ORDER BY th.HistoryEndDt DESC) noteHist OUTER APPLY (SELECT TOP 1 th.HistoryEndDt FROM dbo.wfl_TaskHistory th WITH (NOLOCK) WHERE th.Id = t.Id AND th.AuditNotes IS NOT NULL AND th.AuditNotes = t.AuditNotes ORDER BY th.HistoryEndDt DESC) auditNoteHist WHERE e.CrmId = " + str(crmIdValue[0][0])
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveTaskListCrmId?crmId=" + str(crmIdValue[0][0]), auth=HttpNtlmAuth(username, password))
		dataJson = response.json()[0]
		responseJsonList1 = []
		responseJsonList2 = []
		responseJsonList1.append(dataJson["id"])
		responseJsonList1.append(dataJson["crmId"])
		responseJsonList1.append(dataJson["eid"])
		responseJsonList1.append(dataJson["taskType"])
		responseJsonList1.append(dataJson["resultDescription"])
		responseJsonList2.append(responseJsonList1)
		result = any(elem in sqlResult for elem in responseJsonList2)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskListCrmId", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskListCrmId", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/ReadWorkflowController/RetrieveTaskList by Eid and Task Type Id
	try:
		eidTaskValues = sql_Query("select top 1 b.Eid, a.TaskType_Id from wfl_Task a join wfl_Endpoint b on a.Endpoint_Id = b.Id")
		query = "SELECT e.Eid,e.CrmId,tt.Name [TaskType],t.Description [ResultDescription] FROM dbo.wfl_Endpoint e JOIN dbo.wfl_Task t on t.Endpoint_Id = e.Id JOIN dbo.wfl_TaskType tt on t.TaskType_Id = tt.Id WHERE e.Eid = '" + eidTaskValues[0][0] + "'" + " AND t.TaskType_Id = " + str(eidTaskValues[0][1])
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveTaskList?eid=" + str(eidTaskValues[0][0]) + "&taskType=" + str(eidTaskValues[0][1]), auth=HttpNtlmAuth(username, password))
		dataJson = response.json()[0]
		responseJsonList1 = []
		responseJsonList2 = []
		responseJsonList1.append(dataJson["eid"])
		responseJsonList1.append(dataJson["crmId"])
		responseJsonList1.append(dataJson["taskType"])
		responseJsonList1.append(dataJson["resultDescription"])
		responseJsonList2.append(responseJsonList1)
		result = any(elem in sqlResult for elem in responseJsonList2)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskList by Eid and Task Type Id", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskList by Eid and Task Type Id", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# # API Call for /api/ReadWorkflowController/RetrieveTaskList by Eid
 # try:
  # eidTaskValues = sql_Query("select top 1 b.Eid from wfl_Task a join wfl_Endpoint b on a.Endpoint_Id = b.Id")
  # query = "SELECT e.Eid,e.CrmId,tt.Name [TaskType],t.Description [ResultDescription] FROM dbo.wfl_Endpoint e JOIN dbo.wfl_Task t on t.Endpoint_Id = e.Id JOIN dbo.wfl_TaskType tt on t.TaskType_Id = tt.Id WHERE e.Eid = '" + eidTaskValues[0][0] + "'"
  # sqlResult = sql_Query(query)
  # response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveTaskList?eid=" + str(eidTaskValues[0][0]), auth=HttpNtlmAuth(username, password))
  # print(response.json())
  # dataJson = response.json()[0]
  # responseJsonList1 = []
  # responseJsonList2 = []
  # responseJsonList1.append(dataJson["eid"])
  # responseJsonList1.append(dataJson["crmId"])
  # responseJsonList1.append(dataJson["taskType"])
  # responseJsonList1.append(dataJson["resultDescription"])
  # responseJsonList2.append(responseJsonList1)
  # result = any(elem in sqlResult for elem in responseJsonList2)
  # if (result == true) and (response.status_code == 200):
   # writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskList by Eid", now, "Passed")
   # print(sqlResult)
   # print(responseJsonList2)
   # print(true)
  # else:
   # writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskList by Eid", now, "Failed")
   # print(sqlResult)
   # print(responseJsonList2)
   # print(false)
 # except (ValueError):
  # print("No Response Json")
	
# API Call for /api/ReadWorkflowController/RetrieveAppealStatus
	try:
		crmIdValue = sql_Query("select top 1 b.CrmId from wfl_Task a join wfl_Endpoint b on a.Endpoint_Id = b.Id where a.TaskType_Id in (9)")
		print(crmIdValue[0][0])
		query = "DECLARE @AppealTasks INT, @RdIds INT, @AppealSubmissionQueues INT, @FccWaiver INT DECLARE @AppealSubmissionQueueType_Id BIGINT = (SELECT TOP 1 Id FROM dbo.wfl_SubmissionQueueType WHERE Code = 'Appeal') DECLARE @IdentifiedAppealResultType_Id TINYINT = (SELECT TOP 1 Id FROM dbo.res_ResultType WHERE ResultCode = 'IdentifiedAppeal') DECLARE @AwaitingAppealResultType_Id TINYINT = (SELECT TOP 1 Id FROM dbo.res_ResultType WHERE ResultCode = 'AwaitingAppealApproval') DECLARE @FccWaiverDocumentType_Id BIGINT = (SELECT TOP 1 Id FROM dbo.dat_DocumentType WHERE DocumentTypeCode = 'FCCWAIVER') SELECT @AppealTasks = COUNT(1) FROM dbo.wfl_Endpoint e JOIN dbo.wfl_SubmissionQueue sq ON sq.Endpoint_Id = e.Id LEFT JOIN dbo.wfl_Task t ON t.Endpoint_Id = e.Id WHERE e.CrmId = " + str(crmIdValue[0][0]) + " AND sq.SubmissionQueueType_Id = @AppealSubmissionQueueType_Id SELECT @AppealSubmissionQueues = COUNT(1) FROM dbo.wfl_SubmissionQueue sq WHERE sq.CrmId = " + str(crmIdValue[0][0]) + " AND sq.SubmissionQueueType_Id = @AppealSubmissionQueueType_Id SELECT  @RdIds = COUNT(1) FROM dbo.wfl_Endpoint ie WHERE ie.CrmId = " + str(crmIdValue[0][0]) + " AND ie.RdId IS NOT NULL SELECT @FccWaiver = COUNT(1) FROM dbo.dat_UserDocument ud WHERE ud.CrmId = " + str(crmIdValue[0][0]) + " AND ud.documentType_Id = @FccWaiverDocumentType_Id SELECT CASE WHEN @RdIds = 0 AND @AppealTasks = 0 AND @AppealSubmissionQueues = 0 AND @FccWaiver <> 0 THEN 'SubmitAppeal' WHEN @RdIds > 0 THEN 'AlreadyRegistered' WHEN @AppealTasks > 0 THEN 'HasAppealTasks' ELSE '' END [AppealStatus]"
		sqlResult = sql_Query(query)
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveAppealStatus?crmId=" + str(crmIdValue[0][0]), auth=HttpNtlmAuth(username, password))
		if (sqlResult[0][0] == str(response.json())) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveAppealStatus", now, "Passed")
			print(sqlResult[0][0])
			print(str(response.json()))
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveAppealStatus", now, "Failed")
			print(sqlResult[0][0])
			print(str(response.json()))
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/ReadWorkflowController/RetrievePriorSubmissions
	try:
		sqlResult = sql_Transaction("SET NOCOUNT ON; exec udsp_sub_RetrievePriorSubmissionSummaries @CrmId=625506")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrievePriorSubmissions?crmId=625506", auth=HttpNtlmAuth(username, password))
		
		dataJson = response.json()[0]
		responseJsonList1 = []
		responseJsonList2 = []
		responseJsonList1.append(dataJson["submissionType"])
		responseJsonList1.append(dataJson["name"])
		responseJsonList1.append(dataJson["residentialStreetAddress"])
		responseJsonList1.append(dataJson["registeredStreetAddress"])
		responseJsonList1.append(dataJson["crmId"])
		responseJsonList1.append(dataJson["submission_Id"])
		responseJsonList1.append(dataJson["submissionEntry_Id"])
		responseJsonList1.append(dataJson["submissionQueueHistory_Id"])
		responseJsonList2.append(sqlResult[1][1])
		responseJsonList2.append(sqlResult[1][2])
		responseJsonList2.append(sqlResult[1][3])
		responseJsonList2.append(sqlResult[1][4])
		responseJsonList2.append(sqlResult[1][7])
		responseJsonList2.append(sqlResult[1][8])
		responseJsonList2.append(sqlResult[1][9])
		responseJsonList2.append(sqlResult[1][10])
		result = any(elem in responseJsonList1 for elem in responseJsonList2)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrievePriorSubmissions", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrievePriorSubmissions", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/ReadWorkflowController/RetrieveTaskTypes
	try:
		sqlResult = sql_QueryJsonResults("select a.Id as id, a.Code as code, a.Name as name, a.Description as description, a.IsAutomatic as isAutomatic, a.NeedsAudit as needsAudit, a.IsActive as isActive, a.SortOrder as sortOrder from wfl_TaskType a")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveTaskTypes", auth=HttpNtlmAuth(username, password))
		dataJson = response.json()
		responseJsonList1 = []
		responseJsonList2 = []
		for item in dataJson:
			responseJsonList1.append(item)
		for item in sqlResult:
			responseJsonList2.append(item)
		result = any(elem in responseJsonList2 for elem in responseJsonList1)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskTypes", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveTaskTypes", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/ReadWorkflowController/RetrieveRiskCodes
	try:
		sqlResult = sql_QueryJsonResults("select a.Id as id, a.ResultCode as resultCode, a.Description as description from res_ResultType a where a.Id in (68, 61, 69, 62, 70, 63, 64, 65, 66, 67, 71, 76, 72, 77, 73, 78, 74, 79, 75, 80, 81, 84, 82, 85, 83, 86, 111)")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveRiskCodes", auth=HttpNtlmAuth(username, password))
		dataJson = response.json()
		responseJsonList1 = []
		responseJsonList2 = []
		for item in dataJson:
			responseJsonList1.append(item)
		for item in sqlResult:
			responseJsonList2.append(item)
		result = any(elem in responseJsonList2 for elem in responseJsonList1)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveRiskCodes", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveRiskCodes", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/ReadWorkflowController/RetrieveEmergencyAddresses
	try:
		sqlResult = sql_QueryJsonResults("select * from dat_RegisteredAddress a join wfl_Endpoint b on a.Endpoint_Id = b.Id")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveEmergencyAddresses", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveEmergencyAddresses", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveEmergencyAddresses", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/ReadWorkflowController/RetrieveUserAgreements
	try:
		sqlResult = sql_QueryJsonResults("select * from dat_UserAgreement")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/ReadWorkflowController/RetrieveUserAgreements", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveUserAgreements", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/ReadWorkflowController/RetrieveUserAgreements", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")


def OutreachTools():
# API Call for /api/OutreachToolsController/RetrieveInstalledUsers
	try:
		sqlResult = sql_Transaction("SET NOCOUNT ON; exec udsp_outr_RetrieveInstalledUsers")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/OutreachToolsController/RetrieveInstalledUsers", auth=HttpNtlmAuth(username, password))
		responseCount = len(response.json())
		sqlCount = len(sqlResult)
		if (sqlCount == responseCount) and (response.status_code == 200):
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveInstalledUsers", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveInstalledUsers", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/OutreachToolsController/RetrieveLatestRequestId
	try:
		crmIdValue = sql_Query("SELECT e.CrmId FROM dbo.dat_Person p JOIN dbo.wfl_Endpoint e ON e.CrmId = p.CrmId JOIN dbo.wfl_SubmissionQueue sq ON e.Id = sq.Endpoint_Id LEFT JOIN dbo.dat_RegisteredAddress rega ON rega.Endpoint_Id = e.Id where rega.StreetAddress is not null and sq.RequestID is not null")
		sqlResult = sql_QueryJsonResults("select e.CrmId as crmId, sq.RequestID as requestID, rega.StreetAddress as streetAddress, p.DOB as dob FROM dbo.dat_Person p JOIN dbo.wfl_Endpoint e ON e.CrmId = p.CrmId JOIN dbo.wfl_SubmissionQueue sq ON e.Id = sq.Endpoint_Id LEFT JOIN dbo.dat_RegisteredAddress rega ON rega.Endpoint_Id = e.Id WHERE e.CrmId = " + str(crmIdValue[0][0]))
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/OutreachToolsController/RetrieveLatestRequestId?CrmId=" + str(crmIdValue[0][0]), auth=HttpNtlmAuth(username, password))
		dataJson = response.json()
		responseJsonList1 = []
		responseJsonList2 = []
		for item in dataJson:
			responseJsonList1.append(item)
		for item in sqlResult:
			responseJsonList2.append(item)
		result = any(elem in responseJsonList2 for elem in responseJsonList1)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveLatestRequestId", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveLatestRequestId", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/OutreachToolsController/RetrievePortedOutTdns
	try:
		sqlResult = sql_QueryJsonResults("SELECT e.CrmId as crmId, e.Eid as tdn, pdt.[Description] as action FROM dbo.dat_PortDate pd JOIN dbo.dat_PortDateType pdt ON pd.PortDateType_Id = pdt.Id JOIN dbo.wfl_Endpoint e ON pd.Eid = e.Eid CROSS APPLY (SELECT TOP 1 * FROM dbo.wfl_EndpointHistory eh WITH (NOLOCK) WHERE eh.Eid = e.Eid AND eh.RdId >'' ORDER BY eh.HistoryEndDt DESC) eh WHERE pd.IsActive = 1 AND e.RdId IS NULL")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/OutreachToolsController/RetrievePortedOutTdns", auth=HttpNtlmAuth(username, password))
		dataJson = response.json()
		responseJsonList1 = []
		responseJsonList2 = []
		for item in dataJson:
			responseJsonList1.append(item["crmId"])
			responseJsonList1.append(item["tdn"])
			responseJsonList1.append(item["action"])
		for item in sqlResult:
			responseJsonList2.append(item["crmId"])
			responseJsonList2.append(item["tdn"])
			responseJsonList2.append(item["action"])
		result = any(elem in responseJsonList2 for elem in responseJsonList1)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/OutreachToolsController/RetrievePortedOutTdns", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/OutreachToolsController/RetrievePortedOutTdns", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/OutreachToolsController/RetrieveScrubbedMinutes
	try:
		sqlResult = sql_QueryJsonResults2("SELECT PRC.UserType as userType, PRC.CrmId as crmId, PRC.Tdn as tdn, PRC.SubmissionQueueType as submissionQueueType, PRC.SubmissionQueueStatus as submissionQueueStatus, PRC.TaskType as taskType, SUM( PRC.Mins ) as minutes FROM  VRSRegistration_Settings.dbo.vBilling_ProgressReportCurrentSubmissionTask AS PRC WHERE  PRC.CallCompensable = 0 AND (PRC.UserType NOT LIKE 'Internal%' AND PRC.UserType NOT LIKE 'Hearing%' AND PRC.UserType NOT LIKE 'Company%Hearing%') AND PRC.CallDate >= DATEADD(DAY,-1,CAST(GETUTCDATE() AS DATE)) GROUP BY PRC.CallDate, PRC.UserType, PRC.CRMID, PRC.Tdn, PRC.SubmissionQueueType, PRC.SubmissionQueueStatus, PRC.TaskType order by SUM( PRC.Mins ) desc")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/OutreachToolsController/RetrieveScrubbedMinutes?numberOfDaysToReturn=1", auth=HttpNtlmAuth(username, password))
		dataJson = response.json()
		responseJsonList1 = []
		responseJsonList2 = []
		for item in dataJson:
			responseJsonList1.append(item["userType"])
			responseJsonList1.append(item["crmId"])
			responseJsonList1.append(item["tdn"])
			responseJsonList1.append(item["submissionQueueType"])
			responseJsonList1.append(item["submissionQueueStatus"])
			responseJsonList1.append(item["taskType"])
			responseJsonList1.append(item["minutes"])
		for item in sqlResult:
			responseJsonList2.append(item["userType"])
			responseJsonList2.append(item["crmId"])
			responseJsonList2.append(item["tdn"])
			responseJsonList2.append(item["submissionQueueType"])
			responseJsonList2.append(item["submissionQueueStatus"])
			responseJsonList2.append(item["taskType"])
			responseJsonList2.append(item["minutes"])
		result = any(elem in responseJsonList1 for elem in responseJsonList2)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveScrubbedMinutes", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveScrubbedMinutes", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")

# API Call for /api/OutreachToolsController/RetrieveScrubbedMinutesSummary
	try:
		sqlResult = sql_QueryJsonResults2("SELECT  PRC.UserType as userType, ISNULL(PRC.SubmissionQueueType, '') as submissionQueueType, ISNULL(PRC.SubmissionQueueStatus, '') as submissionQueueStatus, ISNULL(PRC.TaskType, '') as taskType, SUM( PRC.Mins ) as minutes FROM VRSRegistration_Settings.dbo.vBilling_ProgressReportCurrentSubmissionTask AS PRC WHERE  PRC.CallCompensable = 0 AND (PRC.UserType NOT LIKE 'Internal%' AND PRC.UserType NOT LIKE 'Hearing%' AND PRC.UserType NOT LIKE 'Company%Hearing%') AND PRC.CallDate    >= DATEADD(DAY,-1,CAST(GETUTCDATE() AS DATE)) GROUP BY PRC.UserType, PRC.SubmissionQueueType, PRC.SubmissionQueueStatus, PRC.TaskType order by Minutes desc")
		response = requests.get("http://urd-qa.corp.srelay.com/URA/api/OutreachToolsController/RetrieveScrubbedMinutesSummary?numberOfDaysToReturn=1", auth=HttpNtlmAuth(username, password))
		dataJson = response.json()
		responseJsonList1 = []
		responseJsonList2 = []
		for item in dataJson:
			responseJsonList1.append(item["userType"])
			if item["submissionQueueType"] is None:
				item["submissionQueueType"] = ''
				responseJsonList1.append(item["submissionQueueType"])
			else: 
				responseJsonList1.append(item["submissionQueueType"])
			if item["submissionQueueStatus"] is None:
				item["submissionQueueStatus"] = ''
				responseJsonList1.append(item["submissionQueueStatus"])
			else:
				responseJsonList1.append(item["submissionQueueStatus"])
			if item["taskType"] is None:
				item["taskType"] = ''
				responseJsonList1.append(item["taskType"])
			else:
				responseJsonList1.append(item["taskType"])
			responseJsonList1.append(item["minutes"])
		for item in sqlResult:
			responseJsonList2.append(item["userType"])
			responseJsonList2.append(item["submissionQueueType"])
			responseJsonList2.append(item["submissionQueueStatus"])
			responseJsonList2.append(item["taskType"])
			responseJsonList2.append(item["minutes"])
		result = any(elem in responseJsonList1 for elem in responseJsonList2)
		if (result == true) and (response.status_code == 200):
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveScrubbedMinutesSummary", now, "Passed")
			print(true)
		else:
			writeOutTestResults(path, "/api/OutreachToolsController/RetrieveScrubbedMinutesSummary", now, "Failed")
			print(false)
	except (ValueError):
		print("No Response Json")
