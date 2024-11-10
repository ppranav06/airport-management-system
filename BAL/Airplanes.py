from abc import ABC,abstractmethod
from DAL.ManufacturersData import ManufacturersData
from DAL.ModelData import ModelData
from DAL.AirplaneData import AirplaneData
from .Connection import Connection
from .Tests import Tests
tests=Tests()

class Airplanes:
    def __init__(self) -> None:
        self.ManufacturersData=ManufacturersData(Connection())
        self.Models=ModelData(Connection())
        self.Airplanes=AirplaneData(Connection())

    def GetAllManufacturers(self):
        return self.ManufacturersData.GetAllManufacturers()
    
    def GetModels(self,manufacturerID):
        return self.Models.GetModels(manufacturerID)
    
    def GetAirplanes(self,modelID):
        return [AirCraft(testRecord) for testRecord in self.Airplanes.GetAirplanes(modelID)] 

    def GetModelsLookUp(self):
        return self.Models.GetModelLookUp()
    
    def GetAirplaneInfo(self,RegistrationNo):
        return AirCraft(self.Airplanes.GetAirplaneInfo(RegistrationNo))
    
class AirCraft:
    def __init__(self,Details):
        self.Details=Details
        self.State=TestsPendingState(self)
        self.State.refreshState()

    def SetState(self,state):
        self.State=state(self)

class TestsState(ABC):
    def __init__(self,aircraft) -> None:
        self.aircraft=aircraft

    def refreshState(self):
        self.pendingTests=tests.CreateNewTests(self.aircraft.Details[0])
            

            

class TestsPendingState(TestsState):
    def __init__(self,aircraft) -> None:
        super().__init__(aircraft)
        aircraft.status="Tests Pending"

    def refreshState(self):
        super().refreshState()
        if not self.pendingTests:
            self.aircraft.SetState(TestsDoneState)

class TestsDoneState(TestsState):
    def __init__(self,aircraft) -> None:
        super().__init__(aircraft)
        aircraft.status="Tests Done"

    def refreshState(self):
        super().refreshState()
        if self.pendingTests:
            self.aircraft.SetState(TestsPendingState)
