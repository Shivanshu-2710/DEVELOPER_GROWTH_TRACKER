import mysql.connector as ms
db=ms.connect(host="localhost",
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
user_id=int(input("Enter your userid : "))
sh=float(input("Study hours : "))
dq=int(input("Enter dsa questions : "))
gc=int(input("Git Commits : "))
ph=float(input("Enter project hours : "))
pd=input("Enter Date (YYYY-MM-DD) : ")
cursor.execute("insert into daily_progress(user_id,study_hours,dsa_questions,git_commits,project_hours,progress_date) VALUES(%s,%s,%s,%s,%s,%s)",
               (user_id,sh,dq,gc,ph,pd))
db.commit()
print('done')
db.close()