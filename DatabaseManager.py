import sqlite3


class IDatabase():
    def __init__(self) -> None:
        pass


class sqliteData(IDatabase):
    def __init__(self,tableName):
        super().__init__()
        self.tblName = tableName

    def Connect(self):
        connection = sqlite3.connect("covidDataset.db")
        cursor = connection.cursor()
        list = [connection,cursor]
        return list


    def Add(self,Current_Case,RYCase,Death,RYDeath,Total_Doses,RYDoses,Vaccinated,RYPercent):
        conn = self.Connect()
        conn[1].execute(f"INSERT INTO {self.tblName} (Current_Case,Reported_Yesterday_Case,Death,Reported_Yesterday_Death,Total_Doses,Reported_Yesterday_Doses,Vaccinated,Reported_Yesterday_percent) VALUES (?,?,?,?,?,?,?,?)",
                       (Current_Case, RYCase, Death, RYDeath,Total_Doses,RYDoses,Vaccinated,RYPercent))
        conn[0].commit()
        conn[0].close()
        print("işlem Tamamlandı.")

    def getData(self):
        conn = self.Connect()
        conn[1].execute(f"Select * from {self.tblName}")
        data = conn[1].fetchall()
        conn[0].close()
        return data







