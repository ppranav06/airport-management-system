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
    
    def CreateTest(self, test_id, test_name, test_max_score, test_periodicity, test_description="Default description: This is a test."):
        """Creates a new test in the test table."""
        self.TestsData.CreateTest(test_id, test_name, test_max_score, test_periodicity,test_description)
