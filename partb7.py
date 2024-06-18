import sqlite3
con = sqlite3.connect("mydb3.db")
mycursor = con.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS ebill(tcode CHAR(20), cname char(20), mno INT, pmr INT, cmr INT) ")
while(1):
    print("1 For insert data to customer table \n 2. To update customer details \n 3. To calculate customer bill \n 4. For exit")
    c= int(input("Enter your choice "))
    if(c==1):
        print("Enter tariff code : ", end=" ")
        tcode1=input()
        print("Enter customer name : ", end=" ")
        cname1 = input()
        print("Enter meter number : ", end=" ")
        mno1 = int(input())
        print("Enter previous meter reading : ", end=" ")
        pmr1 = int(input())
        print("Enter current meter reading : ", end=" ")
        cmr1 = int(input())
        mycursor.execute('INSERT INTO ebill VALUES ("%s","%s","%i","%i","%i")' % (tcode1,cname1,mno1,pmr1,cmr1))
        print("Value Inserted")
        con.commit()
    elif(c==2):
        print("Enter meter number to update : ",end=" ")
        mno1=int(input())
        sql="SELECT * FROM ebill where mno= '%d' "
        mycursor.execute(sql%mno1)
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        if len(myresult)==0:
            print(f"customer with this meter number (mno1) does not exist")
        else:
            print("enter updated tariff code : ",end=" ")
            tcode1 = input()
            print("Enter updated customer name : ", end=" ")
            cname1 = str(input())
            print("Enter previous meter reading : ", end=" ")
            pmr1 = int(input())
            print("Enter current meter reading : ", end=" ")
            cmr1 = int(input())
            sql="UPDATE ebill SET tcode='%s' , cname='%s' , pmr=%i, cmr=%i where mno=%i "
            mycursor.execute(sql%(tcode1,cname1,pmr1,cmr1,mno1))
            con.commit()
            print(mycursor.rowcount,"record(s) affected ")
    elif(c==3):
        print("enter meter number to calculate bill :",end=" ")
        mno1=int(input())
        sql=" SELECT * FROM ebill where mno= '%d' "
        mycursor.execute(sql%mno1)
        myresult=mycursor.fetchall()
        if len(myresult)==0:
            print(f"customer number {mno1} does not exist ")
        else:
            for row in myresult:
                tcode1=row[0]
                cname1=row[1]
                mno1=row[2]
                pmr1=row[3]
                cmr1=row[4]
                uc=cmr1-pmr1
            if tcode1 == "LT1" or tcode1=="lt1" :
                if uc>=0 and uc<=30:
                    bill=uc*2.0
                elif uc>=31 and uc<=100:
                    bill=(uc-30)*3.5+60
                elif uc >= 101 and uc <= 200:
                    bill=(uc-100)*4.5+305
                else:
                    bill=(uc-200)*5.0+755
            elif tcode1 == "LT2" or tcode1=="lt2" :
                if uc>=0 and uc<=30:
                    bill=uc*3.5
                elif uc>=31 and uc<=100:
                    bill=(uc-30)*5.0+105
                elif uc >= 101 and uc <= 200:
                    bill=(uc-200)*6.0+455
                else:
                    bill=(uc-200)*7.5+1055

            print(f'tariff code is : {tcode1}')
            print(f'customer name is : {cname1}')
            print(f'meter number is : {mno1}')
            print(f'previous meter reading : {pmr1}')
            print(f'current meter reading : {cmr1}')
            print(f'total bill  is : {bill}')

    elif(ch==4):
        break
    else:
        print("invalid chice")

