import oracledb


class TestInfoData:
    def __init__(self,connection) -> None:
        self.connection=connection

    def GetTestInfo(self,RegistrationNo):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetTestsOfPlane', [str(RegistrationNo),result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            self.connection.close()

    def GetTestInfoPerTechnician(self,TechnicianSsn):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetTestsOfTechnician', [str(TechnicianSsn),result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            self.connection.close()

    def InsertTestInfo(self,TestId,RegNo,Ssn,ProposedDate,ActualDate,Hours,score):
        try:
            cursor=self.connection.cursor()
            cursor.callproc('usp_InsertTestInfo', [str(TestId),str(RegNo),str(Ssn),ProposedDate,ActualDate,str(Hours),str(score)])
            
        except Exception as e:
            raise e
        finally:
            self.connection.close()

    