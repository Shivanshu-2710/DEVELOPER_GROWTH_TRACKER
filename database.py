import mysql.connector as ms
db=ms.connect(host='localhost',
              user='root',
              password='Shivanshu@mysql',
                )
cursor=db.cursor()
cursor.execute('DROP DATABASE growth_tracker;')
cursor.execute('CREATE DATABASE growth_tracker;')
cursor.execute('USE growth_tracker;')
cursor.execute('''
CREATE TABLE daily_progress(
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
CREATE TABLE users(
    id INT AUTO_INCREMENT,
    user_id INT,
    user_name varchar(100),
    PRIMARY KEY (id)
);  
''')
print('done')
db.close()