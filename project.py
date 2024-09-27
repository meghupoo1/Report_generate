import mysql.connector
mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
           
         )
mycursor=mydb.cursor()
class TaskList:
    def __init__(self,pid,name,status,skip):
        self.pid=pid
        self.name=name
        self.status=status
        self.skip=skip
    def __str__(self):
        return f'{self.pid},{self.name},{self.status},{self.skip},'
class TaskManager:
    def createDB():
        try:
            mycursor.execute("CREATE DATABASE ToDoList")
            print("DataBase Create Successfully")
        except Exception :
            print("already created DB")
        else:
            print("working fine")
    def useDB():
        try:
            mycursor.execute("use ToDoList")
        except Exception:  
            print("already used DB")
        else:
            print("working fine") 
    def createProgram():
        try:
            mycursor.execute("create table Person(pid int(10),name varchar(30),status varchar(30))") 
            print("table created") 
        except Exception:
            print("already table created ")
        else:
            ("working fine")
    def insertProgram( pid,name, status,skip):
        try:
            sql = "INSERT INTO Person (pid,name, status,skip) VALUES (%s, %s, %s,%s)"
            mycursor.execute(sql, (pid,name,status,skip))
            mydb.commit()
            print("Inserted  successfully")
        except Exception :
            print("Failed to insert data into table:")
        else:
            print("working fine")
         
    def alterTable():
        try:
            sql = "ALTER TABLE Person add column(Timings varchar(20))"
            mycursor.execute(sql)
            mydb.commit()
            print("Altered table successfully") 
        except Exception :
            print("Failed to alter the table:")
        else:
            print("Working fine")
          
    def updateProgram():
        try:
            mycursor.execute("update Person set status ='completedself.timing' where pid=1") 
            mydb.commit()
            print("updated successfully")
        except Exception:
            print("isuess while creating DB")
        else:
            ("working fine")
    def deleteProgram():
        try:
            mycursor.execute("delete from Person  where pid=1")
            mydb.commit()
            print("deleted successfully")
        except Exception:
            print("issue while Deleteing")
        else:
            print("working fine")
tm=TaskManager
tm.createDB()
tm.useDB()
#tm.createProgram()
#tm.insertProgram("1", "Exercise","Completed","NO")
#tm.insertProgram("2", "Breakfast","Pending","yes")
#tm.insertProgram("3", "Lunch","progress","No")
#tm.insertProgram("4", "dinner","progress","yes")
#tm.insertProgram("5", "Swiming","completed","no")
#tm.alterTable()
tm.updateProgram()
#tm.deleteProgram()
#mycursor.close()  # Optional: Close the cursor
#mydb.close()      #Close the database connection
#print("Database connection closed.")


