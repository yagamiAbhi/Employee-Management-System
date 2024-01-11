import sqlite3 as db

con = db.connect('EMS.db')
cur = con.cursor()


def create_table():
    create = 'CREATE TABLE EMPLOYEE (EID INT PRIMARY KEY, ENAME VARCHAR(50), POST VARCHAR(50), SALARY INT)'
    cur.execute(create)
    menu()


def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")

    choice = int(input("Enter your Choice "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        remove_emp()
    elif choice == 3:
        promote_emp()
    elif choice == 4:
        disp_emp()
    elif choice == 5:
        exit(0)
    elif choice == 9:
        create_table()
    else:
        print("Invalid Choice")
        menu()
    cur.close()
    con.close()


def check_eid(eid):
    cur.execute(f'''select * from EMPLOYEE WHERE EID={eid}''')
    rows = cur.fetchall()
    row_count = len(rows)
    if row_count == 1:
        return True
    else:
        return False


def add_employee():
    eid = input("Enter Employee Id : ")
    if check_eid(eid):
        print("Employee already exists\nTry Again\n")
        menu()
    else:
        name = input("Enter Employee Name : ")
        post = input("Enter Employee Post : ")
        salary = input("Enter Employee Salary : ")

        query = 'INSERT INTO EMPLOYEE VALUES (' + eid + ',' + '"' + name + '"' + ',' + '"' + post + '"' + ',' + salary + ')'
        cur.execute(query)

        con.commit()
        print("Employee Added Successfully")
        menu()


def remove_emp():
    eid = input("Enter Employee Id : ")
    if not check_eid(eid):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        query = f"delete from EMPLOYEE where EID = {eid}"
        cur.execute(query)

        con.commit()
        print("Employee Removed Successfully")
        menu()


def promote_emp():
    eid = input("Enter Employee Id : ")
    if not check_eid(eid):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        amt = int(input("Enter increase in Salary"))
        current_sal_sql = f'select SALARY from EMPLOYEE where EID = {eid}'
        cur.execute(current_sal_sql)
        new_sal = cur.fetchone()[0] + amt

        new_sal_sql = f"update EMPLOYEE set SALARY = {new_sal} where EID = {eid}"
        cur.execute(new_sal_sql)

        con.commit()
        print("Employee Promoted Successfully")
        menu()


def disp_emp():
    cur.execute('select * from EMPLOYEE')
    data = cur.fetchall()
    for i in data:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("-----------------------------")
    menu()


menu()
