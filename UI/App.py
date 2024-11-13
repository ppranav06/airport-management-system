import customtkinter as ctk
from .AllAirplaneDetailsPage import AllAirplanesPage
from .AllTechnicianDetailsPage import AllTechnicianDetailsPage
from .AirplaneDetailsPage import AirplaneDetailsPage
from .TechnicianDetailsPage import TechnicianDetailsPage
from .AllTestsPage import AllTestsPage
from .HomePage import HomePage

from BAL.Logger import Logger

ctk.set_appearance_mode('light')
loggerInstance = Logger()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1400x700')
        self.resizable(False,False)
        self.title('Airplane Management System')
        self.report_callback_exception = self.handle_exception
        # self.bind('<Motion>',lambda event:print(event.x))

        self.homePage=HomePage(self)
        self.allAirplanesPage=AllAirplanesPage(self)
        self.LoadHomePage()

    def handle_exception(exception, value, traceback):
        """Handles exceptions after passing them to log"""
        # loggerInstance.log(exception, value, traceback)
        # ctk.CTk.report_callback_exception(exception, value, traceback) # calling the original function
        print(exception, value, traceback)

    def LoadHomePage(self):
        self._ClearRootWindow()
        self.homePage.pack()

    def _ClearRootWindow(self):
        for widget in self.pack_slaves():
            widget.pack_forget()

    def LoadAllAirplanesPage(self):
        self._ClearRootWindow()
        self.allAirplanesPage.pack()

    def LoadAllTechnicianDetailsPage(self):
        self._ClearRootWindow()
        self.allTechnicianDetailsPage=AllTechnicianDetailsPage(self)
        self.allTechnicianDetailsPage.pack()

    def LoadAirplaneDetailsPage(self,RegistrationNo):
        self._ClearRootWindow()
        airplaneDetailsPage=AirplaneDetailsPage(self,RegistrationNo)
        airplaneDetailsPage.pack()

    def LoadTechnicianDetailsPage(self,TechnicianNo):
        self._ClearRootWindow()
        technicianDetailsPage=TechnicianDetailsPage(self,TechnicianNo)
        technicianDetailsPage.pack()


    def LoadTestsPage(self):
        self._ClearRootWindow()
        self.testsPage=AllTestsPage(self)
        self.testsPage.pack()