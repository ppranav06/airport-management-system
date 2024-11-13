from DAL.TestInfoData import TestInfoData
from DAL.TestData import TestData
from .Connection import Connection
from dateutil.relativedelta import relativedelta
import datetime,re


class Tests:
    def __init__(self) -> None:
        self.TestInfoData=TestInfoData(Connection.getInstance())
        self.TestsData=TestData(Connection.getInstance())

    def GetTestInfo(self,RegistrationNo):
        return self.TestInfoData.GetTestInfo(RegistrationNo)

    def GetTestInfoPerTechnician(self,TechnicianSsn):
        return self.TestInfoData.GetTestInfoPerTechnician(TechnicianSsn)
    
    def GetAllTestsData(self):
        return self.TestsData.GetAllTestsData()
    
    def CreateTest(self, test_id, test_name, test_max_score, test_periodicity, test_description="Default description: This is a test."):
        """Creates a new test in the test table."""
        try:
            self.TestsData.CreateTest(test_id, test_name, test_max_score, test_periodicity,test_description)
        except Exception as e:
            raise e

    
    def CreateNewTests(self,RegistrationNo):
        """Creates new test for an airplane in test_info table"""
        allTestsLookUp=self.GetAllTestsData()
        newTests=[]
        LatestTests={}
        testDetails=self.GetTestInfo(RegistrationNo)
        TestsDoneAtleastOnce={x[1] for x in testDetails}
        """Structure of testDetails:
        0: TESTINFO_ID
        1: TEST_ID
        2: AIRPL_REGNO
        3: TECH_SSN
        4: PROPOSED_DATE
        5: ACTUAL_DATE 
        6: HOURS
        7: SCORE
        8: test_name
        9: test_description
        10: test_periodicity (months)
        11: test_max_score
        """
        for row in testDetails:
            currentTestID = row[1]
            actualTestDate = row[5]
            if (currentTestID not in LatestTests) or (LatestTests[currentTestID][5]<actualTestDate):
                LatestTests[currentTestID]=row
            
        for test in LatestTests.values():
            actualTestDate = test[5]
            if (actualTestDate+relativedelta(months=test[10])).date() < datetime.datetime.now().date():
                # 
                newTest=list(test)
                newTest[3]=None
                newTest[4]=(actualTestDate+relativedelta(months=test[10])).date()
                newTest[5]=None
                newTest[6]=None
                newTest[7]=None
                newTests.append(newTest)

        for test in allTestsLookUp:
            if test[0] not in TestsDoneAtleastOnce:
                newTests.append([None,test[0],RegistrationNo,None,datetime.datetime.now().date(),None,None,test[2],test[1],test[3],test[4]])

        return newTests

    def InsertTestInfo(self,TestId,RegNo,Ssn,ProposedDate,ActualDate,Hours,score):
        try:
            self.TestInfoData.InsertTestInfo(TestId,RegNo,Ssn,ProposedDate,ActualDate,Hours,score)  
        except Exception as e:
            raise e

    def UpdateTestData(self,TestID,TestName,Description,Periodicity,MaxScore):
        try:
            self.TestsData.UpdateTestData(TestID,TestName,Description,Periodicity,MaxScore)
        except Exception as e:
            raise e

    def DeleteTest(self,TestID):
        try:
            self.TestsData.DeleteTest(TestID)
        except Exception as e:
            raise e

    