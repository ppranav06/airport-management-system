import oracledb

class ModelData:
    def __init__(self,connection) -> None:
        self.connection=connection

    def GetModels(self,ManufacturerID):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetModels', [str(ManufacturerID),result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except:
            raise Exception('Data wasnt accessed properly')
        finally:
            self.connection.close()

    def GetModelLookUp(self):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetModelsLookUp', [result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except:
            raise Exception('Data wasnt accessed properly')
        finally:
            self.connection.close()

        

    