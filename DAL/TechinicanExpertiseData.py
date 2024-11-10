import oracledb

class TechnicianExpertiseData:
    def __init__(self,connection) -> None:
        self.connection=connection

    def getTechnicianExpertise(self,TechnicianSsn):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetTechnicianExpertise', [str(TechnicianSsn),result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            self.connection.close()