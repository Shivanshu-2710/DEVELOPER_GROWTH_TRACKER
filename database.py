import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
              database='growth_tracker')
cursor=db.cursor()
cursor.execute('''
CREATE TABLE daily_progress2 (
    id INT AUTO_INCREMENT,
    user_id INT,
    study_hours FLOAT,
    dsa_questions INT,
    git_commits INT,
    project_hours FLOAT,
    progress_date DATE,
    PRIMARY KEY (id)
);
''')
cursor.execute('''
CREATE TABLE users2(
    id INT AUTO_INCREMENT,
    user_id INT,
    user_name varchar(100),
    PRIMARY KEY (id)
);  
''')
print('done')
db.close()