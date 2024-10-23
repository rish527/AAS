import mysql.connector

def add_data(id,name):
    conn=mysql.connector.connect(host="localhost",user="root",password="2005",database="aas")
    my_cur=conn.cursor()
    my_cur.execute("insert into students values(%s,%s)",(id,name))
    conn.commit()
    conn.close()
    print("Done")


def del_data(id):
    conn=mysql.connector.connect(host="localhost",user="root",password="2005",database="aas")
    my_cur=conn.cursor()
    # q=("DELETE FROM students WHERE Id=%s")
    my_cur.execute("DELETE FROM students WHERE Id=%s",(id,))
    conn.commit()
    conn.close()
    print("deleted")


def data():
    conn=mysql.connector.connect(host="localhost",user="root",password="2005",database="aas")
    my_cur=conn.cursor()
    my_cur.execute("Select * from students")
    tab=my_cur.fetchall()
    conn.commit()
    conn.close()
    for i in tab:
        print(i)


