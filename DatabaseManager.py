import sqlite3


class IDatabase():
    def __init__(self) -> None:
        pass


class sqliteData(IDatabase):
    def __init__(self,tableName):
        super().__init__()
        self.tblName = tableName

    def Connect(self):
        global list
        connection = sqlite3.connect("covidDataset.db")
        cursor = connection.cursor()
        list = [connection,cursor]


    def Add(self,Current_Case,RYCase,Death,RYDeath,Total_Doses,RYDoses,Vaccinated,RYPercent):
        self.Connect()
        list[1].execute(f"INSERT INTO {self.tblName} (Current_Case,Reported_Yesterday_Case,Death,Reported_Yesterday_Death,Total_Doses,Reported_Yesterday_Doses,Vaccinated,Reported_Yesterday_percent) VALUES (?,?,?,?,?,?,?,?)",
                       (Current_Case, RYCase, Death, RYDeath,Total_Doses,RYDoses,Vaccinated,RYPercent))
        list[0].commit()
        list[0].close()
        print("işlem Tamamlandı.")

    # def Update(self,servName,ip,port,status):
    #     self.Connect()
    #     list[1].execute(f"Update {self.tblName} set ServerName=?,Host=?,Port=?,Status=? Where Port=?",
    #                     (servName,ip,port,status))
    #     list[0].commit()
    #     list[0].close()

    # def UpdateStatus(self,Status,Port):
    #     self.Connect()
    #     list[1].execute(f"Update {self.tblName} set Status=? Where Port=?",
    #                     (Status,Port))
    #     list[0].commit()
    #     list[0].close()


    def Delete(self,Port):
        self.Connect()
        list[1].execute(f"Delete from {self.tblName} Where Port=?",
                        (Port,))
        list[0].commit()
        list[0].close()


    def getData(self):
        self.Connect()
        list[1].execute(f"Select * from {self.tblName}")
        data = list[1].fetchall()
        list[0].close()
        return data
    
    def getData2(self,port):
        self.Connect()
        list[1].execute(f"Select * from {self.tblName} Where port=?",(port,))
        data = list[1].fetchone()
        list[0].close()
        return data






