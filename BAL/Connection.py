import oracledb
import os
from dotenv import load_dotenv



load_dotenv()

class Connection:
    def __init__(self) -> None:
        self.user=os.environ.get('USER')
        self.password=os.environ.get('PASSWORD')
        self.ip=os.environ.get('IP')
        self.port =os.environ.get('PORT')
        self.service_name  =os.environ.get('SERVICE_NAME')

        self.dsn_tns = oracledb.makedsn(self.ip, self.port, service_name=self.service_name)

    def cursor(self):
        self.connection=oracledb.connect(user=self.user,password=self.password,dsn=self.dsn_tns)
        self.cursor=self.connection.cursor()
        return self.cursor
    
    def close(self):
        
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        del self.cursor
        del self.connection
