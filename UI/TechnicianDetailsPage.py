import customtkinter as ctk
import PIL
from BAL.Technician import Technician
from BAL.Tests import Tests
import datetime
from dateutil.relativedelta import relativedelta

from DATA.Data import Data

technician=Technician()
tests=Tests()
rootPage=None
class TechnicianDetailsPage(ctk.CTkFrame):
    def __init__(self, master,TechnicianNumber, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)
        global rootPage
        rootPage=self.master
        
        self.technicianSideFrame=TechnicianSideFrame(self,TechnicianNumber)
        self.technicianSideFrame.pack(side=ctk.LEFT)
        self.technicianSideFrame.pack_propagate(0)

        self.otherDetailsFrame=OtherDetailsFrame(self,TechnicianNumber)
        self.otherDetailsFrame.pack(side=ctk.RIGHT,fill='both')
        
class TechnicianSideFrame(ctk.CTkFrame):
    def __init__(self, master,TechnicianNumber, **kwargs):
        super().__init__(master, **kwargs,height=700,width=250)
        
        

        TechnicianImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\Technician3.jpg'),size=(250,250))
        self.lblImage=ctk.CTkLabel(master=self,image=TechnicianImage,text="")
        self.lblImage.pack()

        self.lblExpertise=ctk.CTkLabel(master=self,text="Expertise",font=ctk.CTkFont(weight='bold'))
        self.lblExpertise.pack()

        self.Details=ExpertiseFrame(self,TechnicianNumber)
        self.Details.pack(fill='x',padx=20)

        self.btnHome=ctk.CTkButton(self,text='Home',command=self.master.master.LoadHomePage)
        self.btnHome.pack(side=ctk.BOTTOM)

        self.btnBack=ctk.CTkButton(self,text='Back',command=self.master.master.LoadAllTechnicianDetailsPage)
        self.btnBack.pack(side=ctk.BOTTOM)

class ExpertiseFrame(ctk.CTkFrame):
    def __init__(self, master,TechnicianNumber, **kwargs):
        super().__init__(master, **kwargs,width=250,corner_radius=5)

        ExpertiseData=technician.GetTechnicianExpertise(TechnicianNumber)
        
        lblExpertiseModel=ctk.CTkLabel(master=self,text='Expertise on: ',font=ctk.CTkFont(weight='bold'))
        lblExpertiseModel.grid(row=0,column=0,padx=10,sticky='w')
        lblExpertiseYears=ctk.CTkLabel(master=self,text='Years',font=ctk.CTkFont(weight='bold'))
        lblExpertiseYears.grid(row=0,column=1,padx=10,sticky='w')
        
        for i in range(len(ExpertiseData)):
            lblExpertiseModelVal=ctk.CTkLabel(master=self,text=f"{ExpertiseData[i][1]} {ExpertiseData[i][0]}")
            lblExpertiseModelVal.grid(row=i+1,column=0,padx=10,sticky='w')
            lblExpertiseYearsVal=ctk.CTkLabel(master=self,text=ExpertiseData[i][2])
            lblExpertiseYearsVal.grid(row=i+1,column=1,padx=10,sticky='e')

class OtherDetailsFrame(ctk.CTkFrame):
    def __init__(self, master,TechnicianNumber, **kwargs):
        super().__init__(master,height=700,width=1100,**kwargs)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=4)

        self.personalDetailsFrame=PersonalDetailsFrame(self,TechnicianNumber)
        self.personalDetailsFrame.grid(row=0,column=0,sticky='news')

        self.testFrame=TestsFrame(self,TechnicianNumber)
        self.testFrame.grid(row=1,column=0,sticky='ewns')
        

class PersonalDetailsFrame(ctk.CTkFrame):
    def __init__(self, master,TechnicianNumber, **kwargs):
        technicianDetails=technician.GetTechnicianData(TechnicianNumber)[0]
        super().__init__(master, **kwargs,width=1000)
        
        self.lblNameVal=ctk.CTkLabel(self,text=technicianDetails[1],
                                     width=1100,
                                     anchor='nw',
                                     font=ctk.CTkFont(size=50,weight='bold',slant='roman'))
        self.lblNameVal.pack(fill='x',padx=20,pady=20)

        self.editableGrid=EditableDetailsGrid(self,technicianDetails)
        self.editableGrid.pack(fill='x',padx=20)


class EditableDetailsGrid(ctk.CTkFrame):
    def __init__(self, master,technicianDetails, **kwargs):
        super().__init__(master, **kwargs,width=1100)
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=6)

        self.Ssn=ctk.StringVar(value=technicianDetails[0])
        self.Address=ctk.StringVar(value=technicianDetails[4])
        self.ContactNo=ctk.StringVar(value=technicianDetails[3])
        self.Salary=ctk.StringVar(value=technicianDetails[2])

        self.newAddress=ctk.StringVar()
        self.newContactNo=ctk.StringVar()
        self.newSalary=ctk.StringVar()


        self.lblSsn=ctk.CTkLabel(self,text='Social Security Number')
        self.lblAddress=ctk.CTkLabel(self,text='Address')
        self.lblContactNumber=ctk.CTkLabel(self,text='Contact Number')
        self.lblSalary=ctk.CTkLabel(self,text='Salary')
        
        self.lblSsn.grid(column=0,row=0,padx=10,sticky='w')
        self.lblAddress.grid(column=0,row=1,padx=10,sticky='w')
        self.lblContactNumber.grid(column=0,row=2,padx=10,sticky='w')
        self.lblSalary.grid(column=0,row=3,padx=10,sticky='w')

        self.lblSsnVal=ctk.CTkLabel(self,textvariable=self.Ssn)
        self.lblAddressVal=ctk.CTkLabel(self,textvariable=self.Address)
        self.lblContactNumberVal=ctk.CTkLabel(self,textvariable=self.ContactNo)
        self.lblSalaryVal=ctk.CTkLabel(self,textvariable=self.Salary)

        self.lblSsnVal.grid(column=1,row=0,padx=10,sticky='w')
        self.lblAddressVal.grid(column=1,row=1,padx=10,sticky='w')
        self.lblContactNumberVal.grid(column=1,row=2,padx=10,sticky='w')
        self.lblSalaryVal.grid(column=1,row=3,padx=10,sticky='w')

        self.txtAddress=ctk.CTkEntry(self,textvariable=self.newAddress)
        self.txtContactNumber=ctk.CTkEntry(self,textvariable=self.newContactNo)
        self.txtSalary=ctk.CTkEntry(self,textvariable=self.newSalary)

        self.btnEdit=ctk.CTkButton(self,text='Edit',command=self.Edit)
        self.btnSave=ctk.CTkButton(self,text='Save',command=self.Save)
        self.btnCancel=ctk.CTkButton(self,text='Cancel',command=lambda:self.Cancel(technicianDetails[0]))

        self.btnEdit.grid(row=4,column=1)

    def Edit(self):
        self.newAddress.set(self.Address.get())    
        self.newContactNo.set(self.ContactNo.get())
        self.newSalary.set(self.Salary.get())

        self.lblAddressVal.grid_forget()
        self.lblContactNumberVal.grid_forget()
        self.lblSalaryVal.grid_forget()

        self.txtAddress.grid(column=1,row=1,padx=10,sticky='w')
        self.txtContactNumber.grid(column=1,row=2,padx=10,sticky='w')
        self.txtSalary.grid(column=1,row=3,padx=10,sticky='w')

        self.btnEdit.grid_forget()
        self.btnSave.grid(row=4,column=0)
        self.btnCancel.grid(row=4,column=1)

    def Save(self):
        self.Address.set(self.newAddress.get())
        self.ContactNo.set(self.newContactNo.get())
        self.Salary.set(self.newSalary.get())
        
        self.txtAddress.grid_forget()
        self.txtContactNumber.grid_forget()
        self.txtSalary.grid_forget()

        self.lblAddressVal.grid(column=1,row=1,padx=10,sticky='w')
        self.lblContactNumberVal.grid(column=1,row=2,padx=10,sticky='w')
        self.lblSalaryVal.grid(column=1,row=3,padx=10,sticky='w')

        self.btnEdit.grid(row=4,column=1)
        self.btnSave.grid_forget()
        self.btnCancel.grid_forget()
    
    def Cancel(self,TechnicianSsn):
        rootPage.LoadTechnicianDetailsPage(TechnicianSsn)

class TestsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,TechnicianNumber, **kwargs):
        super().__init__(master, **kwargs,width=1100)

        TestRecords=tests.GetTestInfoPerTechnician(TechnicianNumber)
        self.TestRows={}
        self.ExpandedPanels={}

        self.lblHeading=ctk.CTkLabel(self,text='Test Performed',
                                     font=ctk.CTkFont(size=30,weight='bold'),
                                     anchor='w')
        self.lblHeading.pack(padx=20,pady=20,fill='x')
        
        for testDetail in TestRecords:
            row=TestRow(self,testDetail)
            row.pack(fill='x',padx=50)
            self.TestRows[testDetail[0]]=row

    def ShowMore(self,TestDetails):
        TestID=TestDetails[0]
        if not TestID in self.ExpandedPanels:
            self.ExpandedPanels[TestID]=TestRowExpansion(self,TestDetails)
            self.ExpandedPanels[TestID].pack(after=self.TestRows[TestID],fill='x',padx=50)
    
    def ShowLess(self,TestID):
        self.ExpandedPanels[TestID].pack_forget()
        del self.ExpandedPanels[TestID]


class TestRow(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,width=1100)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.lblTestNumberVal=ctk.CTkLabel(self,text=TestDetails[1])
        self.lblTestNameVal=ctk.CTkLabel(self,text=TestDetails[8])
        self.lblPlaneVal=ctk.CTkLabel(self,text=TestDetails[2])
        self.lblTestDate=ctk.CTkLabel(self,text=TestDetails[5])
        self.btnMore=ctk.CTkButton(self,text='More',command=lambda:self.master.ShowMore(TestDetails))
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.lblPlaneVal.grid(column=2,row=0)
        self.lblTestDate.grid(column=3,row=0)
        self.btnMore.grid(column=4,row=0)
class TestRowExpansion(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,width=1100,height=300)
        
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=2)
        self.grid_columnconfigure(2,weight=2)
        self.grid_columnconfigure(3,weight=2)

        self.extraDetails=ExtraDetails(self,TestDetails)
        self.extraDetails.grid(column=1,row=0,pady=10,sticky='e',padx=20)

        self.lblDescriptionBox=DescriptionBox(self,TestDetails)
        self.lblDescriptionBox.grid(column=2,row=0,sticky='nsw',pady=10)

        self.btnLess=ctk.CTkButton(self,text='less',command=lambda:self.master.ShowLess(TestDetails[0]))
        self.btnLess.grid(column=3,row=0,sticky='w')

class DescriptionBox(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,
                         height=300,
                         width=400,
                         fg_color='white',
                         corner_radius=5)
        
        self.lblDescription=ctk.CTkLabel(self,text='Description',anchor='w')
        self.lblDescription.pack(fill='x',padx=5)

        self.lblDescriptionVal=ctk.CTkLabel(self,text=TestDetails[9],anchor='w',justify='left')
        self.lblDescriptionVal.pack(fill='x',padx=5)
        

    
class ExtraDetails(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,width=200,height=200,corner_radius=5)
        
        self.lblProposedDate=ctk.CTkLabel(self,text="Proposed Date",anchor='w',justify='left')
        self.lblActualTestDate=ctk.CTkLabel(self,text="Actual Test Date",anchor='w',justify='left')
        self.lblNextExpectedDate=ctk.CTkLabel(self,text="Next Expected Date",anchor='w',justify='left')
        self.lblHoursSpent=ctk.CTkLabel(self,text="Hours Spent",anchor='w',justify='left')
        self.lblScore=ctk.CTkLabel(self,text="Score",anchor='w',justify='left')
        self.lblPeriodicity=ctk.CTkLabel(self,text="Periodicity",anchor='w',justify='left')
        self.lblMaxScore=ctk.CTkLabel(self,text="Max Score",anchor='w',justify='left')

        self.lblProposedDateVal=ctk.CTkLabel(self,text=TestDetails[4],anchor='w',justify='left')
        self.lblActualTestDateVal=ctk.CTkLabel(self,text=TestDetails[5],anchor='w',justify='left')
        self.lblNextExpectedDateVal=ctk.CTkLabel(self,text=TestDetails[5]+relativedelta(months=TestDetails[10]),
                                                 anchor='w',justify='left')
        self.lblHoursSpentVal=ctk.CTkLabel(self,text=str(TestDetails[6])+" hours",anchor='w',justify='left')
        self.lblScoreVal=ctk.CTkLabel(self,text=TestDetails[7],anchor='w',justify='left')
        self.lblPeriodicityVal=ctk.CTkLabel(self,text=TestDetails[10],anchor='w',justify='left')
        self.lblMaxScoreVal=ctk.CTkLabel(self,text=TestDetails[11],anchor='w',justify='left')        
        
        self.lblProposedDate.grid(row=0,column=0,padx=10,sticky='w')
        self.lblActualTestDate.grid(row=1,column=0,padx=10,sticky='w')
        self.lblNextExpectedDate.grid(row=2,column=0,padx=10,sticky='w')
        self.lblHoursSpent.grid(row=3,column=0,padx=10,sticky='w')
        self.lblScore.grid(row=4,column=0,padx=10,sticky='w')
        self.lblPeriodicity.grid(row=5,column=0,padx=10,sticky='w')
        self.lblMaxScore.grid(row=6,column=0,padx=10,sticky='w')

        self.lblProposedDateVal.grid(row=0,column=1,padx=10,sticky='w')
        self.lblActualTestDateVal.grid(row=1,column=1,padx=10,sticky='w')
        self.lblNextExpectedDateVal.grid(row=2,column=1,padx=10,sticky='w')
        self.lblHoursSpentVal.grid(row=3,column=1,padx=10,sticky='w')
        self.lblScoreVal.grid(row=4,column=1,padx=10,sticky='w')
        self.lblPeriodicityVal.grid(row=5,column=1,padx=10,sticky='w')
        self.lblMaxScoreVal.grid(row=6,column=1,padx=10,sticky='w')