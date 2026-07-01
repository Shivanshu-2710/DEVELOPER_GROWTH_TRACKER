import mysql.connector as ms
import datetime
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
def user_exists(u_id):
    cursor.execute("select user_id from daily_progress where user_id=%s",(u_id,))
    record = cursor.fetchall()
    if len(record)==0 :
        return False    
        

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
    sh = dq = gc = ph = 0
    today=datetime.date.today()
    start_date=today-datetime.timedelta(6)
    query1 = '''
select study_hours,
       dsa_questions,
       git_commits,
       project_hours
from daily_progress
where user_id=%s
and progress_date>=%s
order by progress_date desc
'''
    cursor.execute(query1,(u_id,start_date,))
    records = cursor.fetchall()
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
choice=int(input("Enter Your Choice (1/2) :"))
u_id=int(input('Enter USER ID : '))
if user_exists(u_id) is not False:
    if choice==1:
        total_analytics(u_id)
    elif choice==2:
        weekly_analytics(u_id)
    else:
        print('HAHA DUMB INVALID CHOICE ')
else:
    print('USER ID DOES NOT EXIST')