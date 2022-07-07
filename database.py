import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        #Create a cursor 
        self.c = self.conn.cursor()
        #calling Table
        self.create_table1
        self.create_table1
        self.create_table3
    #list to add

    # create a table for page 1
    def create_table1(self):
        self.c.execute("""CREATE TABlE IF NOT EXISTS tab1(
            ItemName text,
            Cost text,
            date text
        )
        """)
        self.conn.commit()
        return "Created"


    # inserting into database for page 1
    def addIntoDB1(self,list):
        self.c.executemany("INSERT INTO tab1 VALUES(?,?,?)",list,)
        self.conn.commit()

    #  Getting the values for table1 
    def fetchData1(self):
        outs = self.c.execute("SELECT rowid,* FROM tab1").fetchall()
        return outs

    def deleteData1(self,taskid):
        self.c.execute("DELETE FROM tab1 where rowid = ?",(taskid,) )
        self.conn.commit() 
        
    # creating table for page 2
    
    def create_table2(self):
        self.c.execute("""CREATE TABlE IF NOT EXISTS tab2(
            ItemName text,
            Cost text,
            date text
        )
        """)
        self.conn.commit()
        return "Created"


    # inserting into database of page 2
    def addIntoDB2(self,list2):
        self.c.executemany("INSERT INTO tab2 VALUES(?,?,?)",list2,)
        self.conn.commit()


    #  Getting the values for page 2
    def fetchData2(self):
        outs = self.c.execute("SELECT rowid,* FROM tab2").fetchall()
        return outs

    def deleteData2(self,taskid2):
        self.c.execute("DELETE FROM tab2 where rowid = ?",(taskid2,) )
        self.conn.commit() 
    
    #tabale for page 3
    def create_table3(self):
        self.c.execute("""CREATE TABlE IF NOT EXISTS tab3(
            ItemName text,
            Cost text,
            date text
        )
        """)
        self.conn.commit()
        return "Created"


    # inserting into database of page 3
    def addIntoDB3(self,list3):
        self.c.executemany("INSERT INTO tab3 VALUES(?,?,?)",list3,)
        self.conn.commit()


    #  Getting the values for page 3
    def fetchData3(self):
        outs = self.c.execute("SELECT rowid,* FROM tab3").fetchall()
        return outs

    def deleteData3(self,taskid3):
        self.c.execute("DELETE FROM tab3 where rowid = ?",(taskid3,) )
        self.conn.commit() 
    def closeconn(self):
        self.conn.close()
# item = "123"
# cost = "123"
# dateTime = "123"

# list =[
#             (item,cost,dateTime)
#         ]

# init = Database()
# # a= init.addIntoDB3(list)
# # del1 = init.deleteData3()
# # del2 = init.deleteData()

# # del3 = init.deleteData3()
# a = init.fetchData1()
# b = init.fetchData2()
# c = init.fetchData3()
# # for item in a:
# #     print(item)
# # for item in b:
# #     print(item)
# # for item in c:
# #     print(item)