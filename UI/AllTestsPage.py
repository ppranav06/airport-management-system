import customtkinter as ctk
from tkinter import messagebox
import PIL,re

from DATA.Data import Data
from BAL.Tests import Tests

# AirplaneData=Data.Airplanes

tests=Tests()
rootPage=None
class AllTestsPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)
        global rootPage
        rootPage=self.master
        
        self.technicianSideFrame=SideFrame(self)
        self.technicianSideFrame.pack(side=ctk.LEFT)
        self.technicianSideFrame.pack_propagate(0)

        self.allTestsFrame=AllTestsFrame(self)
        self.allTestsFrame.pack(fill='x')
        
        
class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=250)

        self.btnHome=ctk.CTkButton(self,text='Home',command=rootPage.LoadHomePage)
        self.btnHome.pack(side=ctk.BOTTOM)
        
        self.btnBack=ctk.CTkButton(self,text='Back',command=rootPage.LoadHomePage)
        self.btnBack.pack(side=ctk.BOTTOM)
        
class AllTestsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1150,fg_color='white')

        testrow=TestsFrame(self)
        testrow.pack(fill='both',pady=3)

        self.btnInsert=ctk.CTkButton(self,text='Create New Test',command=self.PackInsertFrame)
        self.btnInsert.pack()

    def PackInsertFrame(self):
        self.insertFrame=InsertRow(self)
        self.insertFrame.pack(fill='y')
        self.btnInsert.pack_forget()

class InsertRow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=300,width=1150)

        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.grid_columnconfigure(5, weight=1,uniform='a')

        self.rowconfigure((0,1),weight=1)

        self.txtTestId=ctk.CTkEntry(self,placeholder_text="Test Id")
        self.txtTestName=ctk.CTkEntry(self,placeholder_text="Test Name")
        self.txtTestMaxScore=ctk.CTkEntry(self,placeholder_text="Max Score")
        self.txtTestPeriodicity=ctk.CTkEntry(self,placeholder_text="Periodicity")
        self.lblDescription=ctk.CTkLabel(self,text='Enter Description')
        self.txtDescription=ctk.CTkTextbox(self,height=150,width=500)

        self.txtTestId.grid(row=0,column=0)
        self.txtTestName.grid(row=0,column=1)
        self.txtTestMaxScore.grid(row=0,column=2)
        self.txtTestPeriodicity.grid(row=0,column=3)
        self.lblDescription.grid(row=1,column=1,sticky='ne',pady=5,padx=5)
        self.txtDescription.grid(row=1,column=2,pady=5,columnspan=2,padx=10)
        


        # Inner buttons to feed the data into database
        self.btnInsert=ctk.CTkButton(self,text='Create',
                                     command=self.Create)
        self.btnCancel=ctk.CTkButton(self,text='Cancel',
                                     command=self.Cancel)
        
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.grid_columnconfigure(5, weight=1,uniform='a')
        self.grid_columnconfigure(6, weight=1,uniform='a')

        self.btnInsert.grid(column=5,row=0)
        self.btnCancel.grid(column=6,row=0)

    def Create(self):
        """Creates a new test on clicking the 'Create' button"""
        test_id = self.txtTestId.get()
        test_name = self.txtTestName.get()
        test_max_score = self.txtTestMaxScore.get()
        test_periodicity = self.txtTestPeriodicity.get()
        test_description = self.txtDescription.get("0.0", "end")
        # print((test_id, test_name, test_max_score, test_periodicity, test_description))
        try:
            tests.CreateTest(
                test_id, 
                test_name, 
                test_max_score, 
                test_periodicity,
                test_description
            )
            messagebox.showinfo(title="Information", message="Added new test successfully")
            rootPage.LoadTestsPage()
        except Exception as e:
            # need a (better) dialog box here!
            messagebox.showerror(title='ERROR', message=e)
        
    def Cancel(self):
        rootPage.LoadTestsPage()

class HeadingRow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')

        headingFont=ctk.CTkFont(size=15,weight='bold')

        self.lblTestNumberHeading=ctk.CTkLabel(self,text='Test Id',font=headingFont)
        self.lblTestNameHeading=ctk.CTkLabel(self,text='Test Name',font=headingFont)
        self.lblTestMaxScoreHeading=ctk.CTkLabel(self,text='Max Score',font=headingFont)
        self.lblTestPeriodicityHeading=ctk.CTkLabel(self,text='Periodicity',font=headingFont)

        
        self.lblTestNumberHeading.grid(column=0,row=0,pady=20)
        self.lblTestNameHeading.grid(column=1,row=0)
        self.lblTestMaxScoreHeading.grid(column=2,row=0)
        self.lblTestPeriodicityHeading.grid(column=3,row=0)
        # self.btnDescriptionVal=ctk.CTkButton(self,text='Description').grid(column=4,row=0)
    # dummylabel=ctk.CTkLabel(self,text='a').grid(column=4,row=0)

class TestRow(ctk.CTkFrame):
    def __init__(self, master,testDetails, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')

        self.TestName=ctk.StringVar(value=testDetails[1])
        self.MaxScore=ctk.StringVar(value=testDetails[4])
        self.Periodicity=ctk.StringVar(value=str(testDetails[3])+' months')
        self.Description=ctk.StringVar(value=testDetails[2])

        self.newTestName=ctk.StringVar()
        self.newMaxScore=ctk.StringVar()
        self.newPeriodicity=ctk.StringVar()
        self.newDescription=ctk.StringVar()

        self.lblTestNumberVal=ctk.CTkLabel(self,text=testDetails[0])
        self.lblTestNameVal=ctk.CTkLabel(self,textvariable=self.TestName)
        self.lblTestMaxScoreVal=ctk.CTkLabel(self,textvariable=self.MaxScore)
        self.lblTestPeriodicityVal=ctk.CTkLabel(self,textvariable=self.Periodicity)
        self.btnDescriptionVal=ctk.CTkButton(self,text='Description',command=lambda:self.master.ShowMore(testDetails))
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.lblTestMaxScoreVal.grid(column=2,row=0)
        self.lblTestPeriodicityVal.grid(column=3,row=0)
        self.btnDescriptionVal.grid(column=4,row=0)

        self.txtTestName=ctk.CTkEntry(self,textvariable=self.newTestName)
        self.txtTestMaxScore=ctk.CTkEntry(self,textvariable=self.newMaxScore)
        self.txtTestPeriodicity=ctk.CTkEntry(self,textvariable=self.newPeriodicity)

    def Edit(self):
        noOfMonths=int(re.search('^[0-9]*',self.Periodicity.get()).group(0))

        self.newTestName.set(self.TestName.get())
        self.newMaxScore.set(self.MaxScore.get())
        self.newPeriodicity.set(noOfMonths)
        
        self.lblTestNameVal.grid_forget()
        self.lblTestMaxScoreVal.grid_forget()
        self.lblTestPeriodicityVal.grid_forget()
        
        self.txtTestName.grid(row=0,column=1)
        self.txtTestMaxScore.grid(row=0,column=2)
        self.txtTestPeriodicity.grid(row=0,column=3)

    def Save(self):
        self.TestName.set(self.newTestName.get())
        self.MaxScore.set(self.newMaxScore.get())
        self.Periodicity.set(str(self.newPeriodicity.get())+' months')
        
        self.txtTestName.grid_forget()
        self.txtTestMaxScore.grid_forget()
        self.txtTestPeriodicity.grid_forget()
        
        self.lblTestNameVal.grid(row=0,column=1)
        self.lblTestMaxScoreVal.grid(row=0,column=2)
        self.lblTestPeriodicityVal.grid(row=0,column=3)

    def Delete(self):
        self.pack_forget()
        

class TestRowExpansion(ctk.CTkFrame):
    def __init__(self, master,testDetails, **kwargs):
        super().__init__(master, **kwargs,
                         width=1150,
                         height=300)
        
        self.TestNo=testDetails[0]
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=2)
        self.grid_columnconfigure(2,weight=2)
        self.grid_columnconfigure(3,weight=2)
        self.grid_columnconfigure(4,weight=2)
        self.grid_rowconfigure(0,minsize=200)

        # self.extraDetails=ExtraDetails(self,TestNo)
        # self.extraDetails.grid(column=1,row=0,pady=10,sticky='e',padx=20)

        self.descriptionBox=DescriptionBox(self,testDetails)
        self.descriptionBox.grid(column=2,row=0,sticky='nsw',pady=10)

        self.btnLess=ctk.CTkButton(self,text='less',command=lambda:self.master.ShowLess(self.TestNo))
        self.btnLess.grid(column=3,row=0,sticky='w')


        self.btnEdit=ctk.CTkButton(self,text='Edit',command=self.Edit)
        self.btnEdit.grid(column=4,row=0)
        self.btnDelete=ctk.CTkButton(self,text='Delete',command=lambda m=testDetails[0]:self.Delete(m))
        self.btnDelete.grid(column=5,row=0,sticky='w')

        self.btnSave=ctk.CTkButton(self,text='Save',command=lambda m=testDetails[0]:self.Save(m))

    def Save(self,testID):
        try:
            testRow=self.master.TestRows[self.TestNo]
            tests.UpdateTestData(testID,testRow.newTestName.get(),self.descriptionBox.txtDescription.get("0.0", "end"),testRow.newPeriodicity.get(),testRow.newMaxScore.get())
            testRow.Save()
            self.descriptionBox.Save()
            self.btnSave.grid_forget()
            self.btnEdit.grid(column=4,row=0)
        except Exception as e:
            raise e
        

    def Edit(self):
        self.master.TestRows[self.TestNo].Edit()
        self.descriptionBox.Edit()
        self.btnEdit.grid_forget()
        self.btnSave.grid(column=4,row=0)

    def Delete(self,TestID):
        try:
            tests.DeleteTest(TestID)
            self.master.TestRows[self.TestNo].Delete()
            self.pack_forget()
        except Exception as e:
            raise e

class DescriptionBox(ctk.CTkFrame):
    def __init__(self, master,testDetails, **kwargs):
        super().__init__(master, **kwargs,
                         height=250,
                         width=400,
                         fg_color='white',
                         corner_radius=5)
        
        self.lblDescription=ctk.CTkLabel(self,text='Description',anchor='w')
        self.lblDescription.pack(fill='x',padx=5)

        self.Description=testDetails[2]

        # self.lblDescriptionVal=ctk.CTkLabel(self,textvariable=self.Description,anchor='w',justify='left')
        # self.lblDescriptionVal.pack(fill='both',padx=5)

        
        self.txtDescription=ctk.CTkTextbox(self,height=170,width=350,text_color='black')
        self.txtDescription.pack(fill='both')
        self.txtDescription.insert("0.0", self.Description)
        self.txtDescription.configure(state='disabled')

    def Edit(self):
        self.txtDescription.configure(state='normal')
        
    def Save(self):
        self.txtDescription.configure(state='disabled')

    
class ExtraDetails(ctk.CTkFrame):
    def __init__(self, master,TestNo, **kwargs):
        super().__init__(master, **kwargs,width=200,height=200,corner_radius=5)
        
        self.lblProposedDate=ctk.CTkLabel(self,text="Proposed Date",anchor='w',justify='left')
        self.lblActualTestDate=ctk.CTkLabel(self,text="Actual Test Date",anchor='w',justify='left')
        self.lblNextExpectedDate=ctk.CTkLabel(self,text="Next Expected Date",anchor='w',justify='left')
        self.lblHoursSpent=ctk.CTkLabel(self,text="Hours Spent",anchor='w',justify='left')
        self.lblTechnicianNo=ctk.CTkLabel(self,text="Technician No",anchor='w',justify='left')

        self.lblProposedDateVal=ctk.CTkLabel(self,text="14-JUN-2024",anchor='w',justify='left')
        self.lblActualTestDateVal=ctk.CTkLabel(self,text="15-JUN-2024",anchor='w',justify='left')
        self.lblNextExpectedDateVal=ctk.CTkLabel(self,text="15-AUG-2024",anchor='w',justify='left')
        self.lblHoursSpentVal=ctk.CTkLabel(self,text="16 hrs",anchor='w',justify='left')
        self.lblTechnicianNoVal=ctk.CTkLabel(self,text="T47",anchor='w',justify='left')
        
        
        self.lblProposedDate.grid(row=0,column=0,padx=10,sticky='w')
        self.lblActualTestDate.grid(row=1,column=0,padx=10,sticky='w')
        self.lblNextExpectedDate.grid(row=2,column=0,padx=10,sticky='w')
        self.lblHoursSpent.grid(row=3,column=0,padx=10,sticky='w')
        self.lblTechnicianNo.grid(row=4,column=0,padx=10,sticky='w')

        self.lblProposedDateVal.grid(row=0,column=1,padx=10,sticky='w')
        self.lblActualTestDateVal.grid(row=1,column=1,padx=10,sticky='w')
        self.lblNextExpectedDateVal.grid(row=2,column=1,padx=10,sticky='w')
        self.lblHoursSpentVal.grid(row=3,column=1,padx=10,sticky='w')
        self.lblTechnicianNoVal.grid(row=4,column=1,padx=10,sticky='w')
    
    
class TestsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,width=1150,height=400)
        alltests=tests.GetAllTestsData()

        self.TestRows={}
        self.ExpandedPanels={}

        self.lblHeading=ctk.CTkLabel(self,text='AIRCRAFT TESTS',
                                     font=ctk.CTkFont(size=30,weight='bold'))
        self.lblHeading.pack(pady=20)

        columnHeadingRow=HeadingRow(self).pack(fill='x',pady=3,padx=50)
        
        for testData in alltests:
            row=TestRow(self,testData)
            row.pack(fill='x',padx=50)
            self.TestRows[testData[0]]=row
        

    def ShowMore(self,testData):
        TestNo=testData[0]
        if not TestNo in self.ExpandedPanels:
            self.ExpandedPanels[TestNo]=TestRowExpansion(self,testData)
            self.ExpandedPanels[TestNo].pack(after=self.TestRows[TestNo],fill='x',padx=50)
    
    def ShowLess(self,TestNo):
        self.ExpandedPanels[TestNo].pack_forget()
        del self.ExpandedPanels[TestNo]