import pymysql as x
import matplotlib.pyplot as p

q=input("enter your password: ")
exec=True

try:
    db=x.connect(host="localhost", user="root",passwd=q,db="dps")
    print("Connected Successfully!\n")
except:
    print("Password does not match")
    exec=False

#Above function ensures that password can be added first and then the program is executed

while exec:
    print("                                                           ")
    print("============================")
    print("STUDENT REPORT DATABASE")
    print("============================")
    print("Menu")
    print("============================")
    print("1. Generate Table")
    print("2. Add Record")
    print("3. Display Record")
    print("4. Display Bar Graph(s)")
    print("5. Exit")
    c=int(input("Enter Choice:"))

#Generates a premade table
    if c==1: 
        db=x.connect(host="localhost",user="root", passwd=q,db="dps")
        cur=db.cursor()
        cur.execute("create table stu(roll int,name char(20),grade char(5),eng int, phy int, chem int, maths int);")
        db.commit()
        cur.close()
        db.close()

#Adds record to the table generated above
    elif c==2:
        db=x.connect(host="localhost",user="root",passwd=q,db="dps")
        cur=db.cursor()
        cur.execute("insert into stu values(1,'Abhinav','A1', 91,93,87,95);")
        cur.execute("insert into stu values(2,'Aryan','C1',78,80,81,74);")
        cur.execute("insert into stu values(3,'Manan','A2',90,88,85,91);")
        cur.execute("insert into stu values(4,'Paras','B1',84,81,88,90);")
        cur.execute("insert into stu values(5,'Shrey','D1',75,71,76,69);")
        cur.execute("insert into stu values(6,'Udit','B2',81,84,85,79);")
        db.commit()
        cur.close()
        db.close()

#Option to display records
    elif c==3:
        print("1. Display all student records")
        print("2. Display individual student records")
        print("3. Return")
        d=int(input("Enter choice: "))

        #Displays all
        if d==1:
            db=x.connect(host="localhost",user="root",passwd=q,db="dps")
            print("=====================================")
            cur=db.cursor()
            whole=cur.execute("select * from stu;")
            data=cur.fetchall()
            count=cur.rowcount
            print("Total number of students = ", count, "\n")
            print("rollno | name | grade | eng | phy | chem | maths")
            print("=====================================")
            for row in data:
                print(row,sep=" ")  
            cur.close()
            db.close()

        #Displays Individually
        elif d==2:
            db=x.connect(host="localhost",user="root",passwd=q,db="dps")
            cur=db.cursor()
            rr=int(input("Enter Roll No.:"))
            aa=cur.execute("select * from stu where roll='%d';"%(rr))
            data=cur.fetchone()
            print("=====================================")
            print("rollno | name | grade | eng | phy | chem | maths")
            print("=====================================")
            print(data)

        #Returns the program
        elif d==3:
            exit

        #For entering incorrect / non existing option
        else:
            print("----Not a valid choice----")

#Option To display graphs
    elif c==4:
        print("1. Display Bar Graph - Total Student Marks")
        print("2. Display Bar Graph - Average Student Marks")
        print("3. Display Bar Graph - Individual Student Wise")
        print("4. Display Bar Graph - All")
        print("5. Return")
        d=int(input("enter choice: "))
        
        #Displays total student marks graph
        if d==1:
            db=x.connect(host="localhost",user="root",passwd=q,db="dps")
            cur=db.cursor()
            whole=cur.execute("select * from stu;")
            data=cur.fetchall()
            total=[]
            for i in data:
                a=i[3]+i[4]+i[5]+i[6]
                avg=a/4
                total.append(a)

            students=[]

            for i in data:
                b=i[1]
                students.append(b)

            p.bar(students,total,color="yellow",width=0.5, label="stu total marks")
            p.legend()
            p.show()

        #Displays total student average marks graph
        if d==2:
            db=x.connect(host="localhost",user="root",passwd=q,db="dps")
            cur=db.cursor()
            whole=cur.execute("select * from stu;")
            data=cur.fetchall()
            av=[]

            for i in data:
                a=i[3]+i[4]+i[5]+i[6]
                avg=a/4
                av.append(avg)

            students=[]

            for i in data:
                b=i[1]
                students.append(b)

            p.bar(students,av,color="orange", width=0.5, label="stu average marks")
            p.legend()
            p.show()

        #Displays individual student marks graph
        if d==3:
            db=x.connect(host="localhost",user="root",passwd=q,db="dps")
            cur=db.cursor()
            rr=int(input("Enter Roll No.:"))
            aa=cur.execute("select * from stu where roll='%d';"%(rr))
            data=cur.fetchall()

            subj=["Eng","phy","chem","maths"]
            for i in data:
                name=i[1]
                a=i[3]
                b=i[4]
                c=i[5]
                d=i[6]
                marks=[a,b,c,d]

            p.bar(subj,marks,width=0.5,color="green",label=name)
            p.legend()
            p.show()

        #DIsplays all the graphs together   
        if d==4:
            db=x.connect(host="localhost",user="root",passwd=q,db="dps")
            cur=db.cursor()
            whole=cur.execute("select * from stu;")
            data=cur.fetchall()
            total=[]
            av=[]
            for i in data:
                a=i[3]+i[4]+i[5]+i[6]
                avg=a/4
                av.append(avg)
                total.append(a)

            students=[]

            for i in data:
                b=i[1]
                students.append(b)

            p.bar(students,total,color="yellow",width=0.5, label="stu total marks")
            p.bar(students,av,color="orange", width=0.5, label="stu average marks")
            p.legend()
            p.show()

        #Return to prgram
        elif d==5:
            exit
            
        #For entering incorrect / non existing option
        else:
            print("----Not a valid choice----")
                
    #Quit the program      
    elif c==5:
        quit()

    #For entering incorrect / non existing option
    else:
        print("----Not a valid choice----")       
