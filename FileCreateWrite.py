import csv
import os
import os.path
from _datetime import datetime
from win32com.test.testPersist import now


def writeOutTestResults(path, name, now, testResult):
    booleanValue = os.path.isfile(path)
    if booleanValue == True:
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            field = ["API Name", "Date/Time for Test", "Test Result"]
            writer.writerow(field)
            writer.writerow([name, now, testResult])
    elif booleanValue == False:
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["API Name", "Date/Time for Test", "Test Result"]
            writer.writerow(field)
            writer.writerow([name, now, testResult])
