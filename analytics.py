import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()

query='''select study_hours,
            dsa_questions,
            git_commits,
            project_hours
            from daily_progress where user_id=%s'''
def total_analytics(u_id):
    sh=0
    dq=0
    gc=0
    ph=0
    
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

def weekly_analytics(u_id):
    sh=0
    dq=0
    gc=0
    ph=0
    cursor.execute(query,(u_id,))
    records = cursor.fetchmany(7)
    for rows in records:
        sh+=rows[0]
        dq+=rows[1]
        gc+=rows[2]
        ph+=rows[3]

    print("-"*50)
    print(F'WEEKLY STUDY HOURS {sh}')
    print(f'WEEKLY DSA QUESTIONS {dq}')
    print(f"WEEKLY GIT COMMITS {gc}")
    print(f'WEEKLY PROJECT HOURS {ph}')
    print("-"*50)

print("HELLO ")
print("CHOOSE FROM THE FOLLOWING OPTIONS ::")
print('CHOICE 1 : TOTAL ANALYTICS ')
print('CHOICE 2 : WEEKLY ANALYTICS ')
print('CHOICE 3 : EXIT')
choice=int(input("Enter Your Choice (1/2/3) :"))
u_id=int(input('Enter USER ID : '))
if choice==1:
    total_analytics(u_id)
elif choice==2:
    weekly_analytics(u_id)
elif choice==3:
    print("EXITED SUCCESFULLY")
else:
    print('HAHA DUMB INVALID CHOICE ')