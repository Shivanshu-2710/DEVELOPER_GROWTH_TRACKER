import mysql.connector as ms
from datetime import datetime
def validate_non_negative(a):
    if a<0:
        raise ValueError("NEGATIVE VALUES ARE NOT ALLOWED")
    else:
        return a
while True:
    try:
        db=ms.connect(host="localhost",
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
        cursor=db.cursor()
        user_id=int(input("Enter your userid : "))
        user_id=validate_non_negative(user_id)
        sh=float(input("Study hours : "))
        sh=validate_non_negative(sh)
        dq=int(input("Enter dsa questions : "))
        dq=validate_non_negative(dq)
        gc=int(input("Git Commits : "))
        gc=validate_non_negative(gc)
        ph=float(input("Enter project hours : "))
        ph=validate_non_negative(ph)
        pd=input("Enter Date (YYYY-MM-DD) : ")
        pd = datetime.strptime(pd, "%Y-%m-%d")
        print(pd)
        cursor.execute("insert into daily_progress(user_id,study_hours,dsa_questions,git_commits,project_hours,progress_date) VALUES(%s,%s,%s,%s,%s,%s)",
                (user_id,sh,dq,gc,ph,pd))
        db.commit()
        print('DONE')
        break
    except ValueError as e:
        print(e)
    except ms.Error as e:
        print('DATABASE ERROR ',e)
        db.rollback()
    finally:
        db.close()