import sqlite3
conn = sqlite3.connect("Data.db") #Connecting to Data.db

#creating table
conn.execute("create table C2_TABLE (EmployeeID INT PRIMARY KEY,'First Name' TEXT,'Last Name' TEXT,Age INT,Salary TEXT)")

#table data's to be inserted
emp_id = [1,2,3,4,5]
f_name = ["Evelyn","Olivia","Robert","Doug","Leo"]
l_name = ["Grace","Harper","Hall","Judy","Valdez"]
age = [26,28,24,32,22]
Salary = ["280$","320$","310$","370$","270$"]



for i in range(len(emp_id)):
	conn.execute("insert into C2_TABLE values ("+str(emp_id[i])+",'"+f_name[i]+"','"+l_name[i]+"',"+str(age[i])+",'"+Salary[i]+"')")
	print("insert into C2_TABLE values ("+str(emp_id[i])+",'"+f_name[i]+"','"+l_name[i]+"',"+str(age[i])+",'"+Salary[i]+"')")

conn.commit() #committing records in DB 
conn.close()  #closing connection
