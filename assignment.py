import sqlite3

connection = sqlite3.connect('PEOPLE.db')

def CREATE():
    connection.execute('''CREATE TABLE CUSTOMER
    (NAME VARCHAR(255) NOT NULL,
    ID VARCHAR(18) PRIMARY KEY NOT NULL,
    OPEN_DATE DATE(8) NOT NULL,
    LAST_CONSULT DATE(8),
    VACCINATION_TYPE CHAR(5),
    DOCTOR_NAME CHAR(255),
    STATE CHAR(5),
    COUNTRY CHAR(5),
    POST_CODE INT(5),
    DOB DATE(8),
    ACTIVE_CUSTOMER CHAR(1));''')

def CHOICE():
    global d,n,id,od,ld,vid,dn,st,cn,pc,db,fg,ch
    ch=input("You Want To Add Data In Table Manually(Y/N)")
    if ch=='Yes' or ch == 'Y' or ch=='y':
        print(n:=input("Enter Name = "),id:=input("Enter ID = "),od:=input("Enter O_DATE = "),ld:=input("Enter L_DATE = "),vid:=input("Enter VID = "),\
              dn:=input("Enter DNAME = "),st:=input("Enter State = "),cn:=input("Enter Country = "),pc:=input("Enter PCODE = "),\
              db:=input("Enter DOB = "),fg:=input("Enter Flag = "))
        d=[(n,id,od,ld,vid,dn,st,cn,pc,db,fg)]
     
        Data = [('RAHUL', '123457', 20200414, 20200613, 'MVD', 'JADHAV', 'MH', 'IND', 123, 19971213, 'A'),
                ('John', '123458', 20201014, 20201015, 'MVD', '', 'unio', 'CHN', 356, 19971213, 'A'),
                ('Mathew', '123459', 20201018, 20201017, 'MVD', '', 'sant', 'PAK', 456, 19971213, 'A')
                (n, id, od, ld, vid, dn, st, cn, pc, db, fg)]
        connection.executemany("""INSERT OR IGNORE INTO CUSTOMER (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER) \
              VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11 )""", Data)
       
        connection.commit()
    else:
        Data = [('RAHUL', '123457', 20200414, 20200613, 'MVD', 'JADHAV', 'MH', 'IND', 123, 19971213, 'A'),
                ('John', '123458', 20201014, 20201015, 'MVD', '', 'uni', 'CHN', 356, 19971213, 'A'),
                ('Mathew', '123459', 20201018, 20201017, 'MVD', '', 'sant', 'PAK', 456, 19971213, 'A')]
        connection.executemany("""INSERT OR IGNORE INTO CUSTOMER (NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER) \
              VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11 )""", Data)
      
        connection.commit()


def SHOW():
   cursor = connection.execute("SELECT NAME,ID,OPEN_DATE,LAST_CONSULT,VACCINATION_TYPE,DOCTOR_NAME,STATE,COUNTRY,POST_CODE,DOB,ACTIVE_CUSTOMER from CUSTOMER")
   print("NAME\t | ID\t\t | O_Date\t\t | L_Date\t\t | VID\t | D_Name\t | STATE\t | Country\t | P_CODE\t | DOB\t | FLAG")
   for row in cursor:
      print(row[0],"\t","|",row[1],"\t","|",row[2],"\t","|",row[3],"\t","|",row[4],"\t","|",row[5],"\t",
            "|",row[6],"\t\t","|",row[7],"\t","|",row[8],"\t","|",row[9],"\t","|",row[10])

def GROUPBY():
    cursor = connection.execute("SELECT * from CUSTOMER group by COUNTRY")
    for row in cursor:
      
        connection.execute(f"create table if not exists {row[7]} AS SELECT * FROM CUSTOMER where COUNTRY='{row[7]}'")
     
        print(AS:=connection.execute(f"select * from {row[7]}"))
        for row in AS:
            print(f"details of {row[7]}",row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
      


CREATE()
CHOICE()
SHOW()
GOUPBY()
