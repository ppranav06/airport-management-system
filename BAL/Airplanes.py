from DAL.ManufacturersData import ManufacturersData
from DAL.ModelData import ModelData
from DAL.AirplaneData import AirplaneData
from .Connection import Connection

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
        return self.Airplanes.GetAirplanes(modelID)

    def GetModelsLookUp(self):
        return self.Models.GetModelLookUp()
    
    def GetAirplaneInfo(self,RegistrationNo):
        return self.Airplanes.GetAirplaneInfo(RegistrationNo)