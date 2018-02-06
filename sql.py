import pandas as pd
import MySQLdb as dbapi
import sys
import csv

dbServer='srv'
dbPass='pass'
dbUser='user'

db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
sql = 'SELECT * FROM `crashreport.freemake.com`.crashes;'
data = pd.read_sql_query(sql, db)
print('complete')

def dump_sql(sql, filename):
    db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
    cur=db.cursor()
    cur.execute(sql)
    with open(filename, "w", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)
    print('complete')