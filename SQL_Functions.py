import pyodbc

  
def sql_Query(a):
    conn = pyodbc.connect(r'Trusted Connection=yes;' r'Driver=SQL Server;'
                            r'Server=aw2pre-urdsql01.cvpvtfdhjufe.us-west-2.rds.amazonaws.com;'
                            r'Database=URD;')
    cur = conn.cursor()
    res = cur.execute(a)
    # Do something with your result set, for example print out all the results:
    for r in res:
        print(r)
