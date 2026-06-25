import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
cursor.execute('insert into users(name) VALUES(%s)',('Shivanshu',))
db.commit()
print('user added succesfully')
db.close()