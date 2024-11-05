
import oracledb


class ManufacturersData:
    def __init__(self,connection) -> None:
        self.connection=connection
    def GetAllManufacturers(self):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('USP_GETALLMANUFACTURERS', [result_cursor])
            result=result_cursor.getvalue().fetchall()
        except:
            raise Exception('Data wasnt accessed properly')
        finally:
            self.connection.close()
        
        return result



