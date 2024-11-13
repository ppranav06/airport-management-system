import customtkinter as ctk
from tkinter import messagebox
import PIL

from DATA.Data import Data
from BAL.Technician import Technician

technicians = Technician()
rootPage=None
class AllTechnicianDetailsPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)
        global rootPage
        rootPage=self.master
        print(rootPage.report_callback_exception)
        self.technicianSideFrame=SideFrame(self)
        self.technicianSideFrame.pack(side=ctk.LEFT)
        self.technicianSideFrame.pack_propagate(0)

        self.allTechniciansFrame=AllTechniciansFrame(self)
        self.allTechniciansFrame.pack(fill='x')
        
        
class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=250)

        self.btnHome=ctk.CTkButton(self,text='Home',command=self.master.master.LoadHomePage)
        self.btnHome.pack(side=ctk.BOTTOM)
        
        self.btnBack=ctk.CTkButton(self,text='Back',command=self.master.master.LoadHomePage)
        self.btnBack.pack(side=ctk.BOTTOM)
        
class AllTechniciansFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1150,fg_color='white')

        technicianrow=TechniciansFrame(self)
        technicianrow.pack(fill='x',pady=3)

        self.btnInsert=ctk.CTkButton(self,text='Create New Technician',command=self.PackInsertFrame)
        self.btnInsert.pack()

    def PackInsertFrame(self):
        self.insertFrame=InsertRow(self)
        self.insertFrame.pack()
        self.btnInsert.pack_forget()

class InsertRow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,width=1150,height=50)

        self.btnInsert=ctk.CTkButton(self,text='Create',command=self.Create)
        self.btnCancel=ctk.CTkButton(self,text='Cancel')

        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.grid_columnconfigure(5, weight=1,uniform='a')

        self.btnInsert.grid(column=5,row=0)
        self.btnCancel.grid(column=6,row=0)

        self.txtTechnicianSSN=ctk.CTkEntry(self,placeholder_text="SSN")
        self.txtTechnicianName=ctk.CTkEntry(self,placeholder_text="Technician Name")
        self.txtTechnicianSalary=ctk.CTkEntry(self,placeholder_text="Salary")
        self.txtTechnicianPhno=ctk.CTkEntry(self,placeholder_text="Phone No")
        self.txtTechnicianAddress=ctk.CTkEntry(self,placeholder_text="Address")
        # self.txtTechnicianDetails=ctk.CTkTextbox(self,height=300,width=500)
        # self.txtTechnicianDetails.insert("0.0","Details")

        self.txtTechnicianSSN.grid(row=0,column=0)
        self.txtTechnicianName.grid(row=0,column=1)
        self.txtTechnicianSalary.grid(row=0,column=2)
        self.txtTechnicianPhno.grid(row=0,column=3)
        self.txtTechnicianAddress.grid(row=0,column=4)
        # self.txtTechnicianDetails.grid(row=1,column=0)

    def Create(self):
        try:
            technicians.CreateTechnician(
                self.txtTechnicianSSN.get(),
                self.txtTechnicianName.get(),
                self.txtTechnicianSalary.get(),
                self.txtTechnicianPhno.get(),
                self.txtTechnicianAddress.get()
            )
            rootPage.LoadAllTechnicianDetailsPage()
        except Exception as e:
            # raise e
            messagebox.showerror(title='ERROR', message=e)
        
        

class HeadingRow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.grid_columnconfigure(5, weight=1,uniform='a')

        headingFont=ctk.CTkFont(size=13,weight='bold')

        self.lblTechnicianSSN=ctk.CTkLabel(self,text='SSN',font=headingFont)
        self.lblTechnicianName=ctk.CTkLabel(self,text='Technician Name',font=headingFont)
        self.lblTechnicianSalary=ctk.CTkLabel(self,text='Salary',font=headingFont)
        self.lblTechnicianPhno=ctk.CTkLabel(self,text='Phone No',font=headingFont)
        self.lblTechnicianAddress=ctk.CTkLabel(self,text='Address',font=headingFont)

        
        self.lblTechnicianSSN.grid(column=0,row=0,pady=20)
        self.lblTechnicianName.grid(column=1,row=0)
        self.lblTechnicianSalary.grid(column=2,row=0)
        self.lblTechnicianPhno.grid(column=3,row=0)
        self.lblTechnicianAddress.grid(column=4,row=0)
        # self.btnTechnicianDetailsVal=ctk.CTkButton(self,text='Details').grid(column=5,row=0)
    # dummylabel=ctk.CTkLabel(self,text='a').grid(column=4,row=0)

class TechnicianRow(ctk.CTkFrame):
    def __init__(self, master,technicianDetails, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.grid_columnconfigure(5, weight=1,uniform='a')

        self.TechnicianName=ctk.StringVar(value=technicianDetails[1])
        self.TechnicianSalary=ctk.StringVar(value=technicianDetails[2])
        self.TechnicianPhno=ctk.StringVar(value=str(technicianDetails[3]))
        self.TechnicianAddress=ctk.StringVar(value=str(technicianDetails[4]))
        self.TechnicianDetails=ctk.StringVar(value=technicianDetails[2])

        self.newTechnicianName=ctk.StringVar()
        self.newSalary=ctk.StringVar()
        self.newPhno=ctk.StringVar()
        self.newAddress=ctk.StringVar()
        self.newTechnicianDetails=ctk.StringVar()

        self.lblTechnicianSSN=ctk.CTkLabel(self,text=technicianDetails[0])
        self.lblTechnicianName=ctk.CTkLabel(self,textvariable=self.TechnicianName)
        self.lblTechnicianSalary=ctk.CTkLabel(self,textvariable=self.TechnicianSalary)
        self.lblTechnicianPhno=ctk.CTkLabel(self,textvariable=self.TechnicianPhno)
        self.lblTechnicianAddress=ctk.CTkLabel(self,textvariable=self.TechnicianAddress)
        self.btnTechnicianDetailsVal=ctk.CTkButton(self,text='Details',
                                             command=lambda:self.master.master.master.master.master.master.LoadTechnicianDetailsPage(technicianDetails[0]))
        
        self.lblTechnicianSSN.grid(column=0,row=0,pady=20)
        self.lblTechnicianName.grid(column=1,row=0)
        self.lblTechnicianSalary.grid(column=2,row=0)
        self.lblTechnicianPhno.grid(column=3,row=0)
        self.lblTechnicianAddress.grid(column=4,row=0)
        self.btnTechnicianDetailsVal.grid(column=5,row=0)

        self.txtTechnicianName=ctk.CTkEntry(self,textvariable=self.newTechnicianName)
        self.txtTechnicianSalary=ctk.CTkEntry(self,textvariable=self.newSalary)
        self.txtTechnicianPhno=ctk.CTkEntry(self,textvariable=self.newPhno)
        self.txtTechnicianAddress=ctk.CTkEntry(self,textvariable=self.newAddress)
        
    
class TechniciansFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=650,width=1150)
        alltechnicians=technicians.GetAllTechniciansData()

        self.TechnicianRows={}
        self.ExpandedPanels={}

        self.lblHeading=ctk.CTkLabel(self,text='TECHNICIANS',
                                     font=ctk.CTkFont(size=30,weight='bold'))
        self.lblHeading.pack(pady=20)

        columnHeadingRow=HeadingRow(self).pack(fill='x',pady=3,padx=50)
        
        for technicianData in alltechnicians:
            row=TechnicianRow(self,technicianData)
            row.pack(fill='x',padx=50)
            self.TechnicianRows[technicianData[0]]=row
       