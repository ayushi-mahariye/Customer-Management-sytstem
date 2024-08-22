import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Adishi@26",database="customer")
c=mydb.cursor()
login=False
admid=input("Enter Admin Id")
pwd=input("Enter password")
c.execute("select * from admin")
# To retreive data
for row in c:
   if(admid==row[0] and pwd==row[1]):
       login=True
       break
if(login):
    print("Login Successfully")
else:
    print("Incorrect ID or Password")

# To insert data
#mydb.commit()
#print("Admin Login  Successfully at ID :",admid)