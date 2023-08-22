import pyodbc

  
def sql_Transaction(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=aw2pre-urdsql01.cvpvtfdhjufe.us-west-2.rds.amazonaws.com;'
                            r'Database=URD;')
    cursor = conn.cursor()
    cursor.execute(a)
    conn.commit()


def sql_Query(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=aw2pre-urdsql01.cvpvtfdhjufe.us-west-2.rds.amazonaws.com;'
                            r'Database=URD;')
    cursor = conn.cursor()
    cursor.execute(a)
    result = cursor.fetchall()
    resultValue = [list(i) for i in result]
    return resultValue
