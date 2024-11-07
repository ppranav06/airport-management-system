from DAL.TechnicianData import TechnicianData
from DAL.TechinicanExpertiseData import TechnicianExpertiseData

from .Connection import Connection

class Technician:
    def __init__(self) -> None:
        self.technicianData=TechnicianData(Connection())
        self.TechnicianExpertiseData=TechnicianExpertiseData(Connection())


    def GetTechnicianData(self,Ssn):
        return self.technicianData.GetTechnicianData(Ssn)
    
    def GetAllTechniciansData(self):
        return self.technicianData.GetAllTechniciansData()
    
    def GetTechnicianExpertise(self,TechnicianSsn):
        return self.TechnicianExpertiseData.getTechnicianExpertise(TechnicianSsn)