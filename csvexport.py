import csv
import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
while True:
    try:
        u_id=int(input("Enter User Id"))
        break
    except:
        print("PLEASE ENTER VALID VALUES !! (ONLY INTEGERS ARE ALLOWED)")
        continue
cursor.execute('''select user_id,
    study_hours,
    dsa_questions,
    git_commits,
    project_hours,
    progress_date from daily_progress where user_id like %s''',(u_id,))
record=cursor.fetchone()
with open('growthtracker.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['USER_ID','Study_Hours','Dsa_Questions','Git_Commits','Project_Hours','Progress_Date'])
    while record is not None:
        writer.writerow(record)
        record=cursor.fetchone()