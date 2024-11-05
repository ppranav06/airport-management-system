import customtkinter as ctk
import PIL
from datetime import date
from dateutil.relativedelta import relativedelta
from BAL.Airplanes import Airplanes
from BAL.Tests import Tests


from DATA.Data import Data

# AirplaneData=Data.Airplanes
airplanes=Airplanes()
tests=Tests()

class AirplaneDetailsPage(ctk.CTkFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)
        
        self.AirplaneDetails=AirplaneDetailsFrame(self,RegistrationNumber)
        self.AirplaneDetails.pack(side=ctk.LEFT)
        self.AirplaneDetails.pack_propagate(0)


        self.TestDetails=TestsFrame(self,RegistrationNumber)
        self.TestDetails.pack(side=ctk.RIGHT)

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
        super().__init__(master, **kwargs,
                         width=250,
                         corner_radius=5)
        planeDetails=airplanes.GetAirplaneInfo(RegistrationNumber)[0]
        self.lblManufacturer=ctk.CTkLabel(master=self,text='Manufacturer')
        self.lblManufacturer.grid(row=0,column=0,padx=10,sticky='w')
        self.lblManufacturerVal=ctk.CTkLabel(master=self,text=planeDetails[4])
        self.lblManufacturerVal.grid(row=0,column=1,padx=10,sticky='w')

        self.lblModel=ctk.CTkLabel(master=self,text='Model')
        self.lblModel.grid(row=1,column=0,padx=10,sticky='w')
        self.lblModelVal=ctk.CTkLabel(master=self,text=planeDetails[0])
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

class TestsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,RegistrationNumber, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1150)

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

        pendingRow=PendingTestRow(self,test[0])
        pendingRow.pack(fill='x',padx=50)
    def ShowMore(self,testDetails):
        TestID=testDetails[0]
        if not TestID in self.ExpandedPanels:
            self.ExpandedPanels[TestID]=TestRowExpansion(self,testDetails)
            self.ExpandedPanels[TestID].pack(after=self.TestRows[TestID],fill='x',padx=50)
    
    def ShowLess(self,TestID):
        self.ExpandedPanels[TestID].pack_forget()
        del self.ExpandedPanels[TestID]


class TestRow(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
        super().__init__(master, **kwargs,
                         width=1150)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.lblTestNumberVal=ctk.CTkLabel(self,text=TestDetails[0])
        self.lblTestNameVal=ctk.CTkLabel(self,text=TestDetails[7])
        self.lblTestScoreVal=ctk.CTkLabel(self,text=TestDetails[6])
        self.lblTestDate=ctk.CTkLabel(self,text=TestDetails[4])
        self.btnMore=ctk.CTkButton(self,text='More',command=lambda:self.master.ShowMore(TestDetails))
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.lblTestScoreVal.grid(column=2,row=0)
        self.lblTestDate.grid(column=3,row=0)
        self.btnMore.grid(column=4,row=0)

class PendingTestRow(ctk.CTkFrame):
    def __init__(self, master,TestID, **kwargs):
        super().__init__(master, **kwargs,
                         width=1150)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.lblTestNumberVal=ctk.CTkLabel(self,text=1)
        self.lblTestNameVal=ctk.CTkLabel(self,text='Engine Check')
        self.lblTestScoreVal=ctk.CTkEntry(self)
        self.lblTestDate=ctk.CTkLabel(self,text='09-OCT-2024')
        self.btnMore=ctk.CTkButton(self,text='More')
        self.btnSubmit=ctk.CTkButton(self,text='Submit')
        
        self.lblTestNumberVal.grid(column=0,row=0,pady=20)
        self.lblTestNameVal.grid(column=1,row=0)
        self.lblTestScoreVal.grid(column=2,row=0)
        self.lblTestDate.grid(column=3,row=0)
        self.btnMore.grid(column=4,row=0)
        self.btnSubmit.grid(column=5,row=0)

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

        self.lblDescriptionVal=ctk.CTkLabel(self,text=TestDetails[8],
                                            anchor='w',
                                            justify='left')
        self.lblDescriptionVal.pack(fill='x',padx=5)
        

    
class ExtraDetails(ctk.CTkFrame):
    def __init__(self, master,TestDetails, **kwargs):
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
        self.lblTechnicianNo=ctk.CTkLabel(self,text="Technician Ssn",
                                          anchor='w',
                                          justify='left')
        self.lblProposedDateVal=ctk.CTkLabel(self,text=TestDetails[3],
                                             anchor='w',
                                             justify='left')
        self.lblActualTestDateVal=ctk.CTkLabel(self,text=TestDetails[4],
                                               anchor='w',
                                               justify='left')
        self.lblNextExpectedDateVal=ctk.CTkLabel(self,text=TestDetails[4]+relativedelta(months=TestDetails[9]),
                                                 anchor='w',
                                                 justify='left')
        self.lblHoursSpentVal=ctk.CTkLabel(self,text=str(TestDetails[5])+" hours",
                                           anchor='w',
                                           justify='left')
        self.lblTechnicianNoVal=ctk.CTkLabel(self,text=TestDetails[2],
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