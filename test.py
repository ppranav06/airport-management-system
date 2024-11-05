# import customtkinter as ctk

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry('1400x700')
#         self.resizable(False,False)
#         self.title('tinkering in tkinter')

#         self.frame1=ctk.CTkScrollableFrame(self,width=1400,height=300)
#         self.frame1.pack_propagate(0)
#         self.frame1.pack()

#         frame2=ctk.CTkLabel(self.frame1,text='hi',width=100,height=100)
#         frame2.pack()

# app=App()
# app.mainloop()


"""Connecting to Oracle"""

import os
from dotenv import load_dotenv
import oracledb

# load all environment variables
load_dotenv()

con = oracledb.connect(os.environ.get('CONNECTION_STRING'))
cursor = con.cursor()
result_cursor = cursor.var(oracledb.CURSOR)
cursor.callproc('USP_GETALLMANUFACTURERS', [result_cursor])
print(result_cursor.getvalue().fetchall())