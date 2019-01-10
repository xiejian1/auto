from hive.connect import connection

cur = connection()
sql = 'select * from qiang where name like "xiong%"'

cur.execute(sql)

result = cur.fetchone()
print(result[1])