import pyodbc

  
def sql_Transaction(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=aw2pre-urdsql01.cvpvtfdhjufe.us-west-2.rds.amazonaws.com;'
                            r'Database=URD;')
    cursor = conn.cursor()
    cursor.execute(a)
    result = cursor.fetchall()
    if len(result) > 0:
        resultValue = [list(i) for i in result]
        return resultValue


def sql_Query(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=aw2pre-urdsql01.cvpvtfdhjufe.us-west-2.rds.amazonaws.com;'
                            r'Database=URD;')
    cursor = conn.cursor()
    cursor.execute(a)
    result = cursor.fetchall()
    resultValue = [list(i) for i in result]
    return resultValue


def sql_QueryJsonResults(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=aw2pre-urdsql01.cvpvtfdhjufe.us-west-2.rds.amazonaws.com;'
                            r'Database=URD;')
    cursor = conn.cursor()
    cursor.execute(a)
    resultValue = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    return resultValue


def sql_QueryJsonResults2(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=VDV017-HSTSLS01;'
                            r'Database=VRSRegistration_Settings;')
    cursor = conn.cursor()
    cursor.execute(a)
    resultValue = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    return resultValue
