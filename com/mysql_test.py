import pymysql

con = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='python_db',
    charset='utf8'
)

cursor = con.cursor()
sql = 'insert into user (name, age, sex) values (\'%s\', \'%d\', %d)'
cursor.execute(sql % ('mjp', 26, 1))
con.commit()
print('成功插入', cursor.rowcount, '条数据')


