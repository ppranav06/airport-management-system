import oracledb


class TestData:
    def __init__(self,connection) -> None:
        # Connection() object from BAL
        self.connection=connection

    def GetAllTestsData(self):
        try:
            cursor=self.connection.cursor()
            result_cursor = cursor.var(oracledb.CURSOR)
            cursor.callproc('usp_GetAllTests', [result_cursor])
            result=result_cursor.getvalue().fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            self.connection.close()

    def CreateTest(self, test_id, test_name, test_max_score, test_periodicity,test_description):
        """"""
        try:
            cursor = self.connection.cursor()
            cursor.callproc('USP_CreateTest',[test_id, test_name, test_max_score, test_periodicity,test_description])
            try:
                self.connection.connection.commit()
            except AttributeError:
                print(type(self.connection))
        except Exception as e:
            raise e
        finally:
            self.connection.close()