-- PROCEDURES

-- USED TO GET THE 

   set serveroutput on;

CREATE OR REPLACE PROCEDURE usp_GetAllManufacturers (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Manufacturer;
   -- Stores the entire data in cursor
END;
/

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
  FROM MANUFACTURER;