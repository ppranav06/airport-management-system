from DAL.TechnicianData import TechnicianData
from .Connection import Connection

class Technician:
    def __init__(self) -> None:
        self.technicianData=TechnicianData(Connection())

    def GetTechnicianData(self,Ssn):
        print(Ssn)
        return self.technicianData.GetTechnicianData(Ssn)