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