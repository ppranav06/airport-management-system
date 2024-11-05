CREATE OR REPLACE PROCEDURE usp_GetAllManufacturers (
   result_cursor OUT SYS_REFCURSOR
) AS
BEGIN
   OPEN result_cursor FOR SELECT *
                            FROM Manufacturer;
   CLOSE result_cursor;
END;

DECLARE
   cur_result SYS_REFCURSOR;
BEGIN
   USP_GETALLMANUFACTURERS(cur_result);
   FOR rec IN cur_result LOOP
      DBMS_OUTPUT.PUT_LINE('Manufacturer: ' || rec.man_name); -- Adjust based on your columns
   END LOOP;

   -- Close the cursor if you open it explicitly
   CLOSE cur_result;
END;
/



SELECT *
  FROM MANUFACTURER;