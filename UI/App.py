import customtkinter as ctk
from .AllAirplaneDetailsPage import AllAirplanesPage
from .AirplaneDetailsPage import AirplaneDetailsPage
from .TechnicianDetailsPage import TechnicianDetailsPage
from .AllTestsPage import AllTestsPage
from .HomePage import HomePage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1400x700')
        self.resizable(False,False)
        self.title('Airplane Management System')
        # self.bind('<Motion>',lambda event:print(event.x))

        self.allAirplanesPage=AllAirplanesPage(self)
        self.homePage=HomePage(self)
        self.testsPage=AllTestsPage(self)
        self.LoadHomePage()
        # self.allTechnicianDetailsPage=AllTechnicianDetailsPage(self,1)                    #yet to create

    def _ClearRootWindow(self):
        for widget in self.pack_slaves():
            widget.pack_forget()

    def LoadAllAirplanesPage(self):
        self._ClearRootWindow()
        self.allAirplanesPage.pack()

    def LoadAirplaneDetailsPage(self,RegistrationNo):
        self._ClearRootWindow()
        airplaneDetailsPage=AirplaneDetailsPage(self,RegistrationNo)
        airplaneDetailsPage.pack()

    def LoadTechnicianDetailsPage(self,TechnicianNo):
        self._ClearRootWindow()
        technicianDetailsPage=TechnicianDetailsPage(self,TechnicianNo)
        technicianDetailsPage.pack()

    def LoadHomePage(self):
        self._ClearRootWindow()
        self.homePage.pack()

    def LoadTestsPage(self):
        self._ClearRootWindow()
        self.testsPage.pack()