import customtkinter as ctk
from tkinter import messagebox
import PIL,datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from BAL.Airplanes import Airplanes
from BAL.Tests import Tests

# from DATA.Data import Data

# AirplaneData=Data.Airplanes
airplanes=Airplanes()
tests=Tests()
home=None

class AirplaneDetailsPage(ctk.CTkFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)
        global home
        home=self.master

        self.AirplaneDetails=AirplaneDetailsFrame(self,RegistrationNumber)
        self.AirplaneDetails.pack(side=ctk.LEFT)
        self.AirplaneDetails.pack_propagate(0)


        self.TestDetails=TestsFrame(self,RegistrationNumber)
        self.TestDetails.pack()

        self.PendingTestDetails=PendingTestsFrame(self,RegistrationNumber)
        self.PendingTestDetails.pack()

class AirplaneDetailsFrame(ctk.CTkFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,height=700,width=250)
        
        

        PlaneImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\Airplane1.jpeg'),size=(250,250))
        self.lblImage=ctk.CTkLabel(master=self,image=PlaneImage,text="")
        self.lblImage.pack()

        self.lblRegistrationNumber=ctk.CTkLabel(master=self,text="RegistrationNumber: ",anchor='w')
        self.lblRegistrationNumber.pack()
        self.lblRegistrationNumberVal=ctk.CTkLabel(master=self,text=RegistrationNumber)
        self.lblRegistrationNumberVal.pack()

        self.Details=InfoFrame(self,RegistrationNumber)
        self.Details.pack()

        self.btnHome=ctk.CTkButton(self,text='Home',command=self.master.master.LoadHomePage)
        self.btnHome.pack(side=ctk.BOTTOM)

        self.btnBack=ctk.CTkButton(self,text='Back',command=self.master.master.LoadAllAirplanesPage)
        self.btnBack.pack(side=ctk.BOTTOM)


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,width=250,corner_radius=5)
        aircraftObj=airplanes.GetAirplaneInfo(RegistrationNumber)
        planeDetails=aircraftObj.Details
        planeStatus=aircraftObj.status
        self.lblManufacturer=ctk.CTkLabel(master=self,text='Manufacturer')
        self.lblManufacturer.grid(row=0,column=0,padx=10,sticky='w')
        self.lblManufacturerVal=ctk.CTkLabel(master=self,text=planeDetails[4])
        self.lblManufacturerVal.grid(row=0,column=1,padx=10,sticky='w')

        self.lblModel=ctk.CTkLabel(master=self,text='Model')
        self.lblModel.grid(row=1,column=0,padx=10,sticky='w')
        self.lblModelVal=ctk.CTkLabel(master=self,text=planeDetails[3])
        self.lblModelVal.grid(row=1,column=1,padx=10,sticky='w')

        self.lblCapacity=ctk.CTkLabel(master=self,text='Capacity')
        self.lblCapacity.grid(row=2,column=0,padx=10,sticky='w')
        self.lblCapacityVal=ctk.CTkLabel(master=self,text=planeDetails[6])
        self.lblCapacityVal.grid(row=2,column=1,padx=10,sticky='w')

        self.lblRange=ctk.CTkLabel(master=self,text='Range')
        self.lblRange.grid(row=3,column=0,padx=10,sticky='w')
        self.lblRangeVal=ctk.CTkLabel(master=self,text=planeDetails[7])
        self.lblRangeVal.grid(row=3,column=1,padx=10,sticky='w')

        self.lblCruisingSpeed=ctk.CTkLabel(master=self,text='Cruising Speed')
        self.lblCruisingSpeed.grid(row=4,column=0,padx=10,sticky='w')
        self.lblCruisingSpeedVal=ctk.CTkLabel(master=self,text=planeDetails[8])
        self.lblCruisingSpeedVal.grid(row=4,column=1,padx=10,sticky='w')

        self.lblEngineType=ctk.CTkLabel(master=self,text='Engine Type')
        self.lblEngineType.grid(row=5,column=0,padx=10,sticky='w')
        self.lblEngineTypeVal=ctk.CTkLabel(master=self,text=planeDetails[9])
        self.lblEngineTypeVal.grid(row=5,column=1,padx=10,sticky='w')

        self.lblFirstFlight=ctk.CTkLabel(master=self,text='First Flight')
        self.lblFirstFlight.grid(row=6,column=0,padx=10,sticky='w')
        self.lblFirstFlightVal=ctk.CTkLabel(master=self,text=planeDetails[2])
        self.lblFirstFlightVal.grid(row=6,column=1,padx=10,sticky='w')

        self.lblStatus=ctk.CTkLabel(master=self,text='Status')
        self.lblStatus.grid(row=7,column=0,padx=10,sticky='w')
        self.lblStatusVal=ctk.CTkLabel(master=self,text=planeStatus)
        self.lblStatusVal.grid(row=7,column=1,padx=10,sticky='w')
class TestsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,height=350,width=1150)

        testDetails=tests.GetTestInfo(RegistrationNumber)

        self.TestRows={}
        self.ExpandedPanels={}

        self.lblHeading=ctk.CTkLabel(self,text='RECORD HISTORY OF PLANE TESTS',
                                     font=ctk.CTkFont(size=30,weight='bold'))
        self.lblHeading.pack(pady=20)
        
        for test in testDetails:
            row=TestRow(self,test)
            row.pack(fill='x',padx=50)
            self.TestRows[test[0]]=row

        
    def ShowMore(self,testDetails):
        TestRecordID=testDetails[0]
        if not TestRecordID in self.ExpandedPanels:
            self.ExpandedPanels[TestRecordID]=TestRowExpansion(self,testDetails)
            self.ExpandedPanels[TestRecordID].pack(after=self.TestRows[TestRecordID],fill='x',padx=50)
    
    def ShowLess(self,TestRecordID):
        self.ExpandedPanels[TestRecordID].pack_forget()
        del self.ExpandedPanels[TestRecordID]
class PendingTestsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,height=350,width=1150)

        testDetails=tests.GetTestInfo(RegistrationNumber)

        self.PendingTestRows={}
        self.ExpandedPendingTestPanels={}

        self.lblHeading=ctk.CTkLabel(self,text='SCHEDULED TESTS',
                                     font=ctk.CTkFont(size=30,weight='bold'))
        self.lblHeading.pack(pady=20)
        pendingTests=tests.CreateNewTests(RegistrationNumber)
        if pendingTests != None:
            for pendingTest in pendingTests:
                pendingRow=PendingTestRow(self,pendingTest)
                pendingRow.pack(fill='x',padx=50)

    def ShowMore(self,testDetails):
        TestRecordID=testDetails[0]
        if not TestRecordID in self.ExpandedPendingTestPanels:
            self.ExpandedPendingTestPanels[TestRecordID]=TestRowExpansion(self,testDetails)
            self.ExpandedPendingTestPanels[TestRecordID].pack(after=self.PendingTestRows[TestRecordID],fill='x',padx=50)
    
    def ShowLess(self,TestRecordID):
        self.ExpandedPendingTestPanels[TestRecordID].pack_forget()
        del self.ExpandedPendingTestPanels[TestRecordID]

class TestVariablesInsertionFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.txtTestScore=ctk.CTkEntry(self,placeholder_text='Score')
        self.txtTechnicianNo=ctk.CTkEntry(self,placeholder_text='Technician Ssn')
        self.txtHours=ctk.CTkEntry(self,placeholder_text='Hours')
        self.txtTestScore.pack()
        self.txtTechnicianNo.pack()
        self.txtHours.pack()
class TestRow(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.lblTestNumberVal=ctk.CTkLabel(self,text=TestDetails[1])
        self.lblTestNameVal=ctk.CTkLabel(self,text=TestDetails[8])
        self.lblTestScoreVal=ctk.CTkLabel(self,text=TestDetails[7])
        self.lblTestDate=ctk.CTkLabel(self,text=TestDetails[5])
        self.btnMore=ctk.CTkButton(self,text='More',command=lambda:self.master.ShowMore(TestDetails))
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.lblTestScoreVal.grid(column=2,row=0)
        self.lblTestDate.grid(column=3,row=0)
        self.btnMore.grid(column=4,row=0)

class PendingTestRow(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,width=1150)
        self.grid_columnconfigure(0, weight=1,uniform='a')
        self.grid_columnconfigure(1, weight=1,uniform='a')
        self.grid_columnconfigure(2, weight=1,uniform='a')
        self.grid_columnconfigure(3, weight=1,uniform='a')
        self.grid_columnconfigure(4, weight=1,uniform='a')
        self.lblTestNumberVal=ctk.CTkLabel(self,text=TestDetails[1])
        self.lblTestNameVal=ctk.CTkLabel(self,text=TestDetails[8])
        self.testVariablesInsertionFrame=TestVariablesInsertionFrame(self)
        self.lblProposedTestDate=ctk.CTkLabel(self,text=TestDetails[4])
        self.btnSubmit=ctk.CTkButton(self,text='Submit',command=lambda:self.Insert(TestDetails))
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.testVariablesInsertionFrame.grid(column=2,row=0)
        self.lblProposedTestDate.grid(column=3,row=0)
        self.btnSubmit.grid(column=5,row=0)

    def Insert(self,TestDetails):
        try:
            tests.InsertTestInfo(TestDetails[1],
                                 TestDetails[2],
                                 self.testVariablesInsertionFrame.txtTechnicianNo.get(),
                                 TestDetails[4],
                                 datetime.datetime.now().date(),
                                 self.testVariablesInsertionFrame.txtHours.get(),
                                 self.testVariablesInsertionFrame.txtTestScore.get())
            home.LoadAirplaneDetailsPage(TestDetails[2])
        except Exception as e:
            messagebox.showerror(title='ERROR', message=e)

class TestRowExpansion(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,width=1150,height=300)
        
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

        self.lblDescriptionVal=ctk.CTkLabel(self,text=TestDetails[9],
                                            anchor='w',
                                            justify='left')
        self.lblDescriptionVal.pack(fill='x',padx=5)
        

    
# class ExtraDetails(ctk.CTkFrame):
#     def __init__(self, master,TestDetails, **kwargs):
#         super().__init__(master, **kwargs,
#                          width=200,
#                          height=200,
#                          corner_radius=5)
        
#         self.lblProposedDate=ctk.CTkLabel(self,text="Proposed Date",
#                                           anchor='w',
#                                           justify='left')
#         self.lblActualTestDate=ctk.CTkLabel(self,text="Actual Test Date",
#                                             anchor='w',
#                                             justify='left')
#         self.lblNextExpectedDate=ctk.CTkLabel(self,text="Next Expected Date",
#                                               anchor='w',
#                                               justify='left')
#         self.lblHoursSpent=ctk.CTkLabel(self,text="Hours Spent",
#                                         anchor='w',
#                                         justify='left')
#         self.lblTechnicianNo=ctk.CTkLabel(self,text="Technician Ssn",
#                                           anchor='w',
#                                           justify='left')
#         self.lblProposedDateVal=ctk.CTkLabel(self,text=TestDetails[3],
#                                              anchor='w',
#                                              justify='left')
#         self.lblActualTestDateVal=ctk.CTkLabel(self,text=TestDetails[4],
#                                                anchor='w',
#                                                justify='left')
#         self.lblNextExpectedDateVal=ctk.CTkLabel(self,text=TestDetails[4]+relativedelta(months=TestDetails[9]),
#                                                  anchor='w',
#                                                  justify='left')
#         self.lblHoursSpentVal=ctk.CTkLabel(self,text=str(TestDetails[5])+" hours",
#                                            anchor='w',
#                                            justify='left')
#         self.lblTechnicianNoVal=ctk.CTkLabel(self,text=TestDetails[2],
#                                              anchor='w',
#                                              justify='left')
class ExtraDetails(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,
                         width=200,
                         height=200,
                         corner_radius=5)
        
        self.lblProposedDate=ctk.CTkLabel(self,text="Proposed Date",anchor='w',justify='left')
        self.lblActualTestDate=ctk.CTkLabel(self,text="Actual Test Date",anchor='w',justify='left')
        self.lblNextExpectedDate=ctk.CTkLabel(self,text="Next Expected Date",anchor='w',justify='left')
        self.lblHoursSpent=ctk.CTkLabel(self,text="Hours Spent",anchor='w',justify='left')
        self.lblTechnicianNo=ctk.CTkLabel(self,text="Technician Ssn",anchor='w',justify='left')
        self.lblPeriodicity=ctk.CTkLabel(self,text="Periodicity",anchor='w',justify='left')
        self.lblMaxScore=ctk.CTkLabel(self,text="Max Score",anchor='w',justify='left')
        self.lblProposedDateVal=ctk.CTkLabel(self,text=TestDetails[4],anchor='w',justify='left')
        self.lblActualTestDateVal=ctk.CTkLabel(self,text=TestDetails[5],anchor='w',justify='left')
        self.lblNextExpectedDateVal=ctk.CTkLabel(self,text=TestDetails[5]+relativedelta(months=TestDetails[10]),
                                                 anchor='w',justify='left')
        self.lblHoursSpentVal=ctk.CTkLabel(self,text=str(TestDetails[6])+" hours",anchor='w',justify='left')
        self.lblTechnicianNoVal=ctk.CTkLabel(self,text=TestDetails[3],anchor='w',justify='left')
        self.lblPeriodicityVal=ctk.CTkLabel(self,text=TestDetails[10],anchor='w',justify='left')
        self.lblMaxScoreVal=ctk.CTkLabel(self,text=TestDetails[11],anchor='w',justify='left')
        
        
        self.lblProposedDate.grid(row=0,column=0,padx=10,sticky='w')
        self.lblActualTestDate.grid(row=1,column=0,padx=10,sticky='w')
        self.lblNextExpectedDate.grid(row=2,column=0,padx=10,sticky='w')
        self.lblHoursSpent.grid(row=3,column=0,padx=10,sticky='w')
        self.lblTechnicianNo.grid(row=4,column=0,padx=10,sticky='w')
        self.lblPeriodicity.grid(row=5,column=0,padx=10,sticky='w')
        self.lblMaxScore.grid(row=6,column=0,padx=10,sticky='w')

        self.lblProposedDateVal.grid(row=0,column=1,padx=10,sticky='w')
        self.lblActualTestDateVal.grid(row=1,column=1,padx=10,sticky='w')
        self.lblNextExpectedDateVal.grid(row=2,column=1,padx=10,sticky='w')
        self.lblHoursSpentVal.grid(row=3,column=1,padx=10,sticky='w')
        self.lblTechnicianNoVal.grid(row=4,column=1,padx=10,sticky='w')
        self.lblPeriodicityVal.grid(row=5,column=1,padx=10,sticky='w')
        self.lblMaxScoreVal.grid(row=6,column=1,padx=10,sticky='w')