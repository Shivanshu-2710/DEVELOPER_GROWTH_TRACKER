import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
u_id=int(input("Enter USER ID : "))
query='''select study_hours,
        dsa_questions,
        git_commits,
        project_hours,
        progress_date from daily_progress where user_id=%s order by progress_date '''
cursor.execute(query,(u_id,))
records=cursor.fetchall()
for row in records:
    print("-"*50)
    print(f"Study Hours {row[0]}")
    print(f"DSA Questions {row[1]}")
    print(f'Git Commits {row[2]}')
    print(f'Project Hours {row[3]}')
    print(f"Progress Date {row[4]}")
    print("-"*50,end='\n')

db.close()