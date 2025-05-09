
import oracledb
from .Exceptions import *

class ManufacturersData:
    def __init__(self,connection) -> None:
        self.connection=connection
    def GetAllManufacturers(self):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('USP_GETALLMANUFACTURERS', [result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result   
        except:
            raise UnableToAccessData("Data wasn't accessed properly.")
        finally:
            self.connection.close()
        



