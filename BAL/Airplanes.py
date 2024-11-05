from DAL.ManufacturersData import ManufacturersData
from DAL.ModelData import ModelData
from DAL.AirplaneData import AirplaneData
from .Connection import Connection

class Airplanes:
    def __init__(self,connectionString) -> None:
        self.ManufacturersData=ManufacturersData(Connection())
        self.Models=ModelData(Connection())
        self.Airplanes=AirplaneData()

    def GetAllManufacturers(self):
        return self.ManufacturersData.GetAllManufacturers()
    
    def GetModels(self,manufacturerID):
        return self.Models.GetModels(manufacturerID)
    
    def GetModelsLookUp(self):
        return self.Models.GetModelLookUp()
    