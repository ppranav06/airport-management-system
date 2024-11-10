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

    def CreateTechnician(self,v_Ssn,v_Name,v_Salary,v_Phno,v_Address):
        self.technicianData.CreateTechnician(v_Ssn,v_Name,v_Salary,v_Phno,v_Address)
    
    def UpdateTechnician(self,v_Ssn,v_Salary,v_Phno,v_Address):
        self.technicianData.UpdateTechnician(v_Ssn,v_Salary,v_Phno,v_Address)