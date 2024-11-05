from DAL.TestInfoData import TestInfoData
from .Connection import Connection


class Tests:
    def __init__(self) -> None:
        self.TestInfoData=TestInfoData(Connection())

    def GetTestInfo(self,RegistrationNo):
        return self.TestInfoData.GetTestInfo(RegistrationNo)