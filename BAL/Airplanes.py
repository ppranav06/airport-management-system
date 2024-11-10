from abc import ABC,abstractmethod
from DAL.ManufacturersData import ManufacturersData
from DAL.ModelData import ModelData
from DAL.AirplaneData import AirplaneData
from .Connection import Connection
from .Tests import Tests
tests=Tests()
from typing import Iterable, Iterator

class Airplanes:
    def __init__(self) -> None:
        self.ManufacturersData=ManufacturersData(Connection.getInstance())
        self.Models=ModelData(Connection.getInstance())
        self.Airplanes=AirplaneData(Connection.getInstance())

    def GetAllManufacturers(self):
        return self.ManufacturersData.GetAllManufacturers()
    
    def GetModels(self,manufacturerID):
        return self.Models.GetModels(manufacturerID)
    
    def GetAirplanes(self,modelID):
        # return [AirCraft(testRecord) for testRecord in self.Airplanes.GetAirplanes(modelID)]  # use this if iterator does not work
        # facilitating the use of iterators here:
        return AircraftCollection([AirCraft(testRecord) 
                for testRecord in (self.Airplanes.GetAllAirplanes()) 
                if testRecord[1]==modelID])

    def GetModelsLookUp(self):
        return self.Models.GetModelLookUp()
    
    def GetAirplaneInfo(self,RegistrationNo):
        return AirCraft(self.Airplanes.GetAirplaneInfo(RegistrationNo)[0])
    
class AirCraft:
    """AirCraft is the object represent each aeroplane (forgive multiple terms) identified by regno."""
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

class AircraftCollection(Iterable):
    def __init__(self, aircrafts) -> None:
        self._aircrafts = aircrafts

    def __iter__(self) -> Iterator:
        return AircraftIterator(self._aircrafts)

class AircraftIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._length = len(self._collection)
        self._index = 0

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self._index < self._length:
            aircraftobj = self._collection[self._index]
            self._index += 1
            return aircraftobj
        else:
            raise StopIteration
