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
   INSERT INTO Test_Info VALUES ( TestId,
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
   OPEN result_cursor FOR SELECT t.TEST_ID,
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

SELECT *
  FROM TEST_INFO
 WHERE AIRPL_REGNO = 'F-WWDD';
-- SELECT *
--   FROM MANUFACTURER;
COMMIT;