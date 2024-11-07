-- PROCEDURES

-- USED TO GET THE 

   set serveroutput on;

-- Get all the data from tables (with the help of an open cursor)
-- Stores the entire data in cursor
CREATE OR REPLACE PROCEDURE usp_GetAllManufacturers (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Manufacturer;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllModels (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Model;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllAirplanes (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Airplane;

END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllTechnicians (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Technician;

END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllTests (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Test;
   -- Stores the template tests in cursor
END;
/

CREATE OR REPLACE PROCEDURE usp_GetAirplanes (
   modelID       IN MODEL.Model_Id%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                                                   FROM Airplane
                           WHERE model_id = modelID;
END;
/
CREATE OR REPLACE PROCEDURE usp_GetAirplaneInfo (
   modelID       IN MODEL.Model_Id%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT a.Regno,
                                 m.model_Id,
                                 a.First_Flight,
                                 m.Model_Name,
                                 man.MAN_NAME,
                                 m.Nickname,
                                 m.Capacity,
                                 m.Range,
                                 m.Cruising_Speed,
                                 m.Engine_Type
                                                   FROM Airplane a
                                                   JOIN Model m
                                                 ON m.model_id = a.model_id
                                                   JOIN MANUFACTURER man
                                                 ON man.MAN_ID = m.MANUFACTURER_ID
                           WHERE a.REGNO = modelID;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetModels (
   manufacturerID IN MANUFACTURER.MAN_ID%TYPE,
   result_cursor  OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                                                   FROM Model
                           WHERE MANUFACTURER_ID = manufacturerID;
END;
/
CREATE OR REPLACE PROCEDURE usp_GetTechnician (
   SsnInput      IN Technician.Ssn%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                                                   FROM TECHNICIAN
                           WHERE SSN = SsnInput;
END;
/
CREATE OR REPLACE PROCEDURE usp_InsertTestInfo (
   TestId       IN Test_Info.Test_Id%TYPE,
   RegNo        IN Test_Info.Airpl_Regno%TYPE,
   Ssn          IN Test_Info.Tech_Ssn%TYPE,
   ProposedDate IN Test_Info.Proposed_Date%TYPE,
   ActualDate   IN Test_Info.Actual_Date%TYPE,
   Hours        IN Test_Info.Hours%TYPE,
   score        IN Test_Info.Score%TYPE
) AS
BEGIN
   INSERT INTO Test_Info (
      Test_Id,
      Airpl_Regno,
      Tech_Ssn,
      Proposed_Date,
      Actual_Date,
      Hours,
      Score
   ) VALUES ( TestId,
              RegNo,
              Ssn,
              ProposedDate,
              ActualDate,
              Hours,
              score );
END;
/

CREATE OR REPLACE PROCEDURE usp_GetTestsOfPlane (
   RegNo         IN Airplane.regNo%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT i.TESTINFO_ID,
                                 t.TEST_ID,
                                 i.AIRPL_REGNO,
                                 i.TECH_SSN,
                                 i.PROPOSED_DATE,
                                 i.ACTUAL_DATE,
                                 i.HOURS,
                                 i.SCORE,
                                 t.TEST_NAME,
                                 t.TEST_DESCRIPTION,
                                 t.TEST_PERIODICITY,
                                 t.TEST_MAX_SCORE
                                                   FROM TEST_INFO i
                                                   JOIN TEST t
                                                 ON i.TEST_ID = t.TEST_ID
                           WHERE Airpl_Regno = RegNo;
END;
/
CREATE OR REPLACE PROCEDURE usp_GetTestsOfTechnician (
   TechSsn       IN Technician.Ssn%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT i.TESTINFO_ID,
                                 t.TEST_ID,
                                 i.AIRPL_REGNO,
                                 i.TECH_SSN,
                                 i.PROPOSED_DATE,
                                 i.ACTUAL_DATE,
                                 i.HOURS,
                                 i.SCORE,
                                 t.TEST_NAME,
                                 t.TEST_DESCRIPTION,
                                 t.TEST_PERIODICITY,
                                 t.TEST_MAX_SCORE
                                                   FROM TEST_INFO i
                                                   JOIN TEST t
                                                 ON i.TEST_ID = t.TEST_ID
                           WHERE i.TECH_SSN = TechSsn;
END;
/

-- Procedures to insert data (tests)

CREATE OR REPLACE PROCEDURE USP_CreateTest (
   v_test_id          IN TEST.test_id%TYPE,
   v_test_name        IN TEST.test_name%TYPE,
   v_test_max_score   IN TEST.test_max_score%TYPE,
   v_test_periodicity IN TEST.test_periodicity%TYPE,
   v_test_description IN TEST.test_description%TYPE
) IS
BEGIN
   INSERT INTO TEST (
      test_id,
      test_name,
      test_max_score,
      test_periodicity,
      test_description
   ) VALUES ( v_test_id,
              v_test_name,
              v_test_max_score,
              v_test_periodicity,
              v_test_description );
-- EXCEPTION
--    WHEN OTHERS THEN
--    DBMS_OUTPUT.PUT_LINE  (SQLERRM);
END;
/

CREATE OR REPLACE PROCEDURE USP_DeleteTest (
   v_test_id IN TEST.test_id%TYPE
) AS
BEGIN
   DELETE FROM test
    WHERE TEST_ID = v_test_id;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetTechnicianExpertise (
   TechnicianSsn IN Technician_Expertise.Tech_Ssn%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT mo.MODEL_NAME,
                                 ma.MAN_NAME,
                                 t.YEARS_OF_EXPERIENCE
                                                   FROM Technician_Expertise t
                                                   JOIN Model mo
                                                 ON t.AIRPLANE_MODEL = mo.model_Id
                                                   JOIN Manufacturer ma
                                                 ON ma.Man_Id = mo.MANUFACTURER_ID
                           WHERE Tech_Ssn = TechnicianSsn;
END;
/
-- CREATE OR REPLACE PROCEDURE USP_EditTest(
--    v_test_id IN TEST.test_id%TYPE
-- ) AS 
-- BEGIN
--    DELETE FROM test WHERE TEST_ID=v_test_id;
-- END;
-- /



-- Testing the stored procedures

DECLARE
   res SYS_REFCURSOR;
   REC MANUFACTURER%ROWTYPE;
BEGIN
   -- Call the stored procedure, passing the cursor variable
   USP_GETALLMANUFACTURERS(res);
   LOOP
      FETCH res INTO REC;
      EXIT WHEN res%NOTFOUND;
      DBMS_OUTPUT.PUT_LINE('Manufacturer: ' || rec.man_name); -- Adjust based on your columns
   END LOOP;
   CLOSE res;  -- Not always necessary, but good practice
EXCEPTION
   WHEN OTHERS THEN
      -- Handle any error that occurs
      DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/

DECLARE
   v_test_id          TEST.test_id%TYPE := 'T011';
   v_test_name        TEST.test_name%TYPE := 'OXYGEN MASK TEST';
   v_test_description TEST.test_description%TYPE := 'CHECKS IF OXYGEN MASKS ARE PROPERLY INSTALLED';
   v_test_periodicity TEST.test_periodicity%TYPE := 12;
   v_test_max_score   TEST.test_max_score%TYPE := 100;
BEGIN
   USP_CreateNewTest(
      v_test_id,
      v_test_name,
      v_test_description,
      v_test_periodicity,
      v_test_max_score
   );
END;
/


SELECT *
  FROM TEST_INFO
 WHERE AIRPL_REGNO = 'F-WWDD';
-- SELECT *
--   FROM MANUFACTURER;
COMMIT;