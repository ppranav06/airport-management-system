import oracledb

class TechnicianData:
    def __init__(self,connection) -> None:
        self.connection=connection

    def GetTechnicianData(self,Ssn):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetTechnician', [str(Ssn),result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            self.connection.close()
    
    def GetAllTechniciansData(self):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetAllTechnicians', [result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            self.connection.close()

    def CreateTechnician(self,v_Ssn,v_Name,v_Salary,v_Phno,v_Address):
        try:
            cursor=self.connection.cursor()
            cursor.callproc('usp_CreateTechnician', [str(v_Ssn),str(v_Name),str(v_Salary),str(v_Phno),str(v_Address)])
        except Exception as e:
            raise e
        finally:
            self.connection.close()
    def UpdateTechnician(self,v_Ssn,v_Salary,v_Phno,v_Address):
        try:
            cursor=self.connection.cursor()
            cursor.callproc('usp_UpdateTechnician', [str(v_Ssn),str(v_Salary),str(v_Phno),str(v_Address)])
        except Exception as e:
            raise e
        finally:
            self.connection.close()
    
    