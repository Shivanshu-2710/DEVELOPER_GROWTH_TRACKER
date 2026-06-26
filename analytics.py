import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
sh=0
dq=0
gc=0
ph=0
u_id=int(input('Enter USER ID : '))
query='''select study_hours,
        dsa_questions,
        git_commits,
        project_hours
        from daily_progress where user_id=%s'''
cursor.execute(query,(u_id,))
records = cursor.fetchall()
for rows in records:
    sh+=rows[0]
    dq+=rows[1]
    gc+=rows[2]
    ph+=rows[3]

print("-"*50)
print(F'TOTAL STUDY HOURS {sh}')
print(f'TOTAL DSA QUESTIONS {dq}')
print(f"TOTAL GIT COMMITS {gc}")
print(f'TOTAL PROJECT HOURS {ph}')
print("-"*50)