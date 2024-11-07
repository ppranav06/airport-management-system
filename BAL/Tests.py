from DAL.TestInfoData import TestInfoData
from DAL.TestData import TestData
from .Connection import Connection
from dateutil.relativedelta import relativedelta
import datetime


class Tests:
    def __init__(self) -> None:
        self.TestInfoData=TestInfoData(Connection())
        self.TestsData=TestData(Connection())

    def GetTestInfo(self,RegistrationNo):
        return self.TestInfoData.GetTestInfo(RegistrationNo)

    def GetTestInfoPerTechnician(self,TechnicianSsn):
        return self.TestInfoData.GetTestInfoPerTechnician(TechnicianSsn)
    
    def GetAllTestsData(self):
        return self.TestsData.GetAllTestsData()
    
    def CreateTest(self, test_id, test_name, test_max_score, test_periodicity, test_description="Default description: This is a test."):
        """Creates a new test in the test table."""
        self.TestsData.CreateTest(test_id, test_name, test_max_score, test_periodicity,test_description)

    
    def CreateNewTests(self,RegistrationNo):
        """Creates new test for an airplane in test_info table"""
        newTests=[]
        LatestTests={}
        testDetails=self.GetTestInfo(RegistrationNo)
        for i in testDetails:
            if i[1] not in LatestTests:
                LatestTests[i[1]]=i
            else:
                if LatestTests[i[1]][5]<i[5]:
                    LatestTests[i[1]]=i
        for test in LatestTests.values():
            if (test[5]+relativedelta(months=test[10])).date()<datetime.datetime.now().date():
                newTest=list(test)
                newTest[3]=None
                newTest[4]=(test[5]+relativedelta(months=test[10])).date()
                newTest[5]=None
                newTest[6]=None
                newTest[7]=None
                newTests.append(newTest)

        return newTests

    def InsertTestInfo(self,TestId,RegNo,Ssn,ProposedDate,ActualDate,Hours,score):
        self.TestInfoData.InsertTestInfo(TestId,RegNo,Ssn,ProposedDate,ActualDate,Hours,score)  

    