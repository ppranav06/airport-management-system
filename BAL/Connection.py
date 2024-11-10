import oracledb
import os
from dotenv import load_dotenv
from .Exceptions import *


load_dotenv()

class Connection:
    __Instance=None
    def __init__(self):
        if Connection.__Instance != None:
            raise Exception("This class is a singleton!")
        else:
            Connection.__Instance = self

            self.user=os.environ.get('USER')
            self.password=os.environ.get('PASSWORD')
            self.ip=os.environ.get('IP')
            self.port =os.environ.get('PORT')
            self.service_name  =os.environ.get('SERVICE_NAME')

            try:
                self.dsn_tns = oracledb.makedsn(self.ip, self.port, service_name=self.service_name)
            except Exception as e:
                raise e

    def cursor(self):
        try:
            self.connection=oracledb.connect(user=self.user,password=self.password,dsn=self.dsn_tns)
            self.cursor=self.connection.cursor()
            return self.cursor
        except Exception as e:
            raise e
    
    def close(self):
        
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        del self.cursor
        del self.connection

    def getInstance():
        if Connection.__Instance==None:
            Connection.__Instance=Connection()
        return Connection.__Instance

