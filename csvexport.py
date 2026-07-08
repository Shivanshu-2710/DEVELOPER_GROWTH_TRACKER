import csv
import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
u_id=int(input("Enter User Id"))
cursor.execute('''select user_id,
    study_hours,
    dsa_questions,
    git_commits,
    project_hours,
    progress_date from daily_progress where user_id like %s''',(u_id,))
with open('growthtracker.csv','w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['USER_ID','Study_Hours','Dsa_Questions','Git_Commits','Projecta_Hours','Progress_Date'])
record=cursor.fetchone()
while record is not None:
    with open('growthtracker.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(record)
        record=cursor.fetchone()