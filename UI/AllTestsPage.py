import customtkinter as ctk
import PIL

from DATA.Data import Data

AirplaneData=Data.Airplanes

class AllTestsPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)
        
        self.technicianSideFrame=SideFrame(self)
        self.technicianSideFrame.pack(side=ctk.LEFT)
        self.technicianSideFrame.pack_propagate(0)

        self.allTestsFrame=AllTestsFrame(self)
        self.allTestsFrame.pack(fill='x')
        
        
class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=250)

        self.btnHome=ctk.CTkButton(self,text='Home',command=self.master.master.LoadHomePage)
        self.btnHome.pack(side=ctk.BOTTOM)
        
class AllTestsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1150,fg_color='white')

        for i in range(10):
            testrow=TestsFrame(self,100)
            testrow.pack(fill='x',pady=3)
        
# class TestRow(ctk.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs,height=30,width=1150)
#         self.grid_columnconfigure((0,1),weight=1)
#         self.lblTestVal=ctk.CTkLabel(self,text='Test1',width=1150)
        
#         self.lblTestVal.grid(row=0,column=0)

class HeadingRow(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='b')

        headingFont=ctk.CTkFont(size=15,weight='bold')

        self.lblTestNumberHeading=ctk.CTkLabel(self,text='Test Id',font=headingFont)
        self.lblTestNameHeading=ctk.CTkLabel(self,text='Test Name',font=headingFont)
        self.lblTestMaxScoreHeading=ctk.CTkLabel(self,text='Max Score',font=headingFont)
        self.lblTestPeriodicityHeading=ctk.CTkLabel(self,text='Periodicity',font=headingFont)

        
        self.lblTestNumberHeading.grid(column=0,row=0,pady=20)
        self.lblTestNameHeading.grid(column=1,row=0)
        self.lblTestMaxScoreHeading.grid(column=2,row=0)
        self.lblTestPeriodicityHeading.grid(column=3,row=0)
        self.btnDescriptionVal=ctk.CTkButton(self,text='Description').grid(column=4,row=0)
    # dummylabel=ctk.CTkLabel(self,text='a').grid(column=4,row=0)

class TestRow(ctk.CTkFrame):
    def __init__(self, master,TestNo, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='b')

        self.TestName=ctk.StringVar(value='EngineCheck')
        self.MaxScore=ctk.StringVar(value=10)
        self.Periodicity=ctk.StringVar(value='5 months')
        self.Description=ctk.StringVar(value='Description')

        self.newTestName=ctk.StringVar()
        self.newMaxScore=ctk.StringVar()
        self.newPeriodicity=ctk.StringVar()
        self.newDescription=ctk.StringVar()

        self.lblTestNumberVal=ctk.CTkLabel(self,text=1)
        self.lblTestNameVal=ctk.CTkLabel(self,textvariable=self.TestName)
        self.lblTestMaxScoreVal=ctk.CTkLabel(self,textvariable=self.MaxScore)
        self.lblTestPeriodicityVal=ctk.CTkLabel(self,textvariable=self.Periodicity)
        self.btnDescriptionVal=ctk.CTkButton(self,text='Description',command=lambda:self.master.ShowMore(TestNo))
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.lblTestMaxScoreVal.grid(column=2,row=0)
        self.lblTestPeriodicityVal.grid(column=3,row=0)
        self.btnDescriptionVal.grid(column=4,row=0)

        

class TestRowExpansion(ctk.CTkFrame):
    def __init__(self, master,TestNo, **kwargs):
        super().__init__(master, **kwargs,
                         width=1150,
                         height=300)
        
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=2)
        self.grid_columnconfigure(2,weight=2)
        self.grid_columnconfigure(3,weight=2)
        self.grid_rowconfigure(0,minsize=200)

        # self.extraDetails=ExtraDetails(self,TestNo)
        # self.extraDetails.grid(column=1,row=0,pady=10,sticky='e',padx=20)

        self.lblDescriptionBox=DescriptionBox(self,TestNo)
        self.lblDescriptionBox.grid(column=2,row=0,sticky='nsw',pady=10)

        self.btnLess=ctk.CTkButton(self,text='less',command=lambda:self.master.ShowLess(TestNo))
        self.btnLess.grid(column=3,row=0,sticky='w')

        self.btnEdit=ctk.CTkButton(self,text='Edit')
        self.btnEdit.grid(column=4,row=0)

class DescriptionBox(ctk.CTkFrame):
    def __init__(self, master,TestNo, **kwargs):
        super().__init__(master, **kwargs,
                         height=300,
                         width=400,
                         fg_color='white',
                         corner_radius=5)
        
        self.lblDescription=ctk.CTkLabel(self,text='Description',anchor='w')
        self.lblDescription.pack(fill='x',padx=5)

        self.lblDescriptionVal=ctk.CTkLabel(self,text='This is a Test done to make sure that the engine is\n running fine and all okkkkkkkkkk okkkkk and okkkkkkkkk !!!!',
                                            anchor='w',
                                            justify='left')
        self.lblDescriptionVal.pack(fill='both',padx=5)
        

    
class ExtraDetails(ctk.CTkFrame):
    def __init__(self, master,TestNo, **kwargs):
        super().__init__(master, **kwargs,
                         width=200,
                         height=200,
                         corner_radius=5)
        
        self.lblProposedDate=ctk.CTkLabel(self,text="Proposed Date",
                                          anchor='w',
                                          justify='left')
        self.lblActualTestDate=ctk.CTkLabel(self,text="Actual Test Date",
                                            anchor='w',
                                            justify='left')
        self.lblNextExpectedDate=ctk.CTkLabel(self,text="Next Expected Date",
                                              anchor='w',
                                              justify='left')
        self.lblHoursSpent=ctk.CTkLabel(self,text="Hours Spent",
                                        anchor='w',
                                        justify='left')
        self.lblTechnicianNo=ctk.CTkLabel(self,text="Technician No",
                                          anchor='w',
                                          justify='left')
        self.lblProposedDateVal=ctk.CTkLabel(self,text="14-JUN-2024",
                                             anchor='w',
                                             justify='left')
        self.lblActualTestDateVal=ctk.CTkLabel(self,text="15-JUN-2024",
                                               anchor='w',
                                               justify='left')
        self.lblNextExpectedDateVal=ctk.CTkLabel(self,text="15-AUG-2024",
                                                 anchor='w',
                                                 justify='left')
        self.lblHoursSpentVal=ctk.CTkLabel(self,text="16 hrs",
                                           anchor='w',
                                           justify='left')
        self.lblTechnicianNoVal=ctk.CTkLabel(self,text="T47",
                                             anchor='w',
                                             justify='left')
        
        
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
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,
                         height=700,
                         width=1150)
        self.TestRows={}
        self.ExpandedPanels={}

        self.lblHeading=ctk.CTkLabel(self,text='AIRCRAFT TESTS',
                                     font=ctk.CTkFont(size=30,weight='bold'))
        self.lblHeading.pack(pady=20)

        columnHeadingRow=HeadingRow(self).pack(fill='x',pady=3,padx=50)
        
        for i in range(10):
            row=TestRow(self,i)
            row.pack(fill='x',padx=50)
            self.TestRows[i]=row

    def ShowMore(self,TestNo):
        if not TestNo in self.ExpandedPanels:
            self.ExpandedPanels[TestNo]=TestRowExpansion(self,TestNo)
            self.ExpandedPanels[TestNo].pack(after=self.TestRows[TestNo],fill='x',padx=50)
    
    def ShowLess(self,TestNo):
        self.ExpandedPanels[TestNo].pack_forget()
        del self.ExpandedPanels[TestNo]