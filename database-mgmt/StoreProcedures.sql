-- PROCEDURES

-- USED TO GET THE 

set serveroutput on;

-- Get all the data from tables (with the help of an open cursor)
-- Stores the entire data in cursor
CREATE OR REPLACE PROCEDURE usp_GetAllManufacturers (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT * FROM Manufacturer;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllModels (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT * FROM Model;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllAirplanes (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT * FROM Airplane;

END;
/

CREATE OR REPLACE PROCEDURE usp_GetAllTests ( 
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT * FROM Test;
   -- Stores the template tests in cursor
END;
/

CREATE OR REPLACE PROCEDURE usp_GetAirplanes (
   modelID IN MODEL.Model_Id%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR 
      SELECT * FROM Airplane
      WHERE model_id = modelID;
END;
/

CREATE OR REPLACE PROCEDURE usp_GetModels (
   manufacturerID IN MANUFACTURER.MAN_ID%TYPE,
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR 
      SELECT * FROM Model
      WHERE MANUFACTURER_ID=manufacturerID;
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

-- SELECT *
--   FROM MANUFACTURER;