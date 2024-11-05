from DAL.TestInfoData import TestInfoData
from DAL.TestData import TestData
from .Connection import Connection


class Tests:
    def __init__(self) -> None:
        self.TestInfoData=TestInfoData(Connection())
        self.TestsData=TestData(Connection())

    def GetTestInfo(self,RegistrationNo):
        return self.TestInfoData.GetTestInfo(RegistrationNo)
    
    def GetAllTestsData(self):
        return self.TestsData.GetAllTestsData()