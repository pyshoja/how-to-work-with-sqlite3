

import sqlite3


cn=sqlite3.connect('test_pyshoja.db')
cr=cn.cursor()
cr.execute('''CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY,
    name TEXT,
    family text,
    age int);
''')
cn.commit()
a=(3,'test3','shoja3',25)
number1=[(1,'test1','shoja1',60),(2,'test2','shoja2',40),a]
cr.executemany('''insert into users(id,name,family,age) values(?,?,?,?)''',number1)
cn.commit()




#This is for function writing ...
def new():
    x=(4,'test4','shoja4',15)

    number2=[(5,'test5','shoja5',10),x]
    cr.executemany('''insert into users (id,name,family,age) values(?,?,?,?)''',number2)
    cn.commit()

new()
