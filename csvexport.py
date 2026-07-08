import csv
import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
u_id=int(input("Enter User Id"))
cursor.execute('select * from daily_progress where user_id like %s',(u_id,))
records=cursor.fetchall()
with open('growthtracker.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(['USER_ID','Study_Hours','Dsa_Questions','Git_Commits','Projecta_Hours','Progress_Date'])
    writer.writerows(records)