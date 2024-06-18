import sqlite3
con = sqlite3.connect('employee.db')
cursor = con.cursor()

def employe_exist(empid):
    sql='''create table if not exists employee(empid integer primary key,empname varchar(10),salary int)'''
    cursor.execute(sql)
    data = (empid,)
    sql="select * from employee where empid = ?"
    cursor.execute(sql,data)
    result=cursor.fetchall()
    if len(result)>0:
        return True
    else:
        return False
def add_employee():
    empid=int(input("Enter Employe ID : "))
    if(employe_exist(empid)==True):
        print("Employee already exist \n Try Again \n")
    else:
        empname=input("Enter employee Name: ")
        salary=int(input("Enter employee salary : "))
        data=(empid,empname,salary)
        sql="Insert or replace into employee values(?,?,?)"
        cursor.execute(sql,data)
        con.commit()
        print("Employee Added successfully")
def display_employee():
    min= input("Enter min Salary : ")
    max = input("Enter max Salary: ")
    sql="select * from employee where salary between ? and ? "
    data=(min,max)
    cursor.execute(sql,data)
    r=cursor.fetchall()
    if len(r)>0:
        for i in r:
            print("Employee ID : ",i[0])
            print("Employee Name : ", i[1])
            print("Employee Salary : ", i[2])
            print("___________________________________")
    else:
        print("Record Not exists ")
def search_employee():
    empid=input("Enter employee Id to be searched")
    sql='select * from employee where empid=?'
    data=(empid,)
    cursor.execute(sql,data)
    r=cursor.fetchone()
    if(r):
        print("Employee ID : ", r[0])
        print("Employee Name : ", r[1])
        print("Employee Salary : ", r[2])
        print("___________________________________")
    else:
        print("Record not Found")
def menu():
    print("Select")
    print("1. To Add New Employee")
    print("2. To search Employee")
    print("3. To fetch employee details whose salary lies within a certain range")
    print("4. To exit")
    ch=int(input("Enter your choice : "))
    if (ch == 1) :
        add_employee()
    elif ch==2:
        search_employee()
    elif ch==3:
        display_employee()
    elif ch==4:
        exit()
    else:
        print("Invalid choice")
    menu()
menu()

