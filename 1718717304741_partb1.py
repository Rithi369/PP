class employee:

     def get_data(self):
         self.emp_no=int(input("Enter employee number: "))
         self.namame=input("Enter name: ")
         self.design=input("Enter designation: ")
         self.dept=input("Enter department: ")
         self.age=input("Enter age: ")
         self.basic=input("Enter basic salary: ")

     def display(self):
         print(self.emp_no,"\t",self.namame,"\t",self.design,"\t",self.dept,"\t",self.age,"\t",self.basic)

     def search(self,id):
         if id==self.emp_no:
             return True
         else:
             return False
n=int(input("Enter the number of employee "))
lst=[]
for i in range(n):
    e1=employee()
    e1.get_data()
    lst.append(e1)
while True:
    print("1.To deisplay employee information \n 2.Search for employee")
    ch=int(input("Enter your choice"))
    if ch==1:
        print("Empne\tname\tDesignation\tdepartment\tage\tsalary")
        for e in lst:
            e.display()
    elif ch==2:
        id=int(input("Enter the employee number to be searched "))
        for i in lst:
            found=i.search(id)
            if found:
                print("Employee found they are ")
                i.display()
                break
        else:
                print("Employee details not found: ")
    else:
            print("invalid choice")
            exit(0)