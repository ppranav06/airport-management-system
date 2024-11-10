-- creating the schema
DROP SEQUENCE Model_Id_Seq;
DROP TABLE Test_Info;
DROP TABLE Test;
DROP TABLE Technician_Expertise;
DROP TABLE Technician;
DROP TABLE Airplane;
DROP TABLE Model;
DROP TABLE Manufacturer;


CREATE TABLE Manufacturer (
   Man_Id   INTEGER PRIMARY KEY,
   Man_Name VARCHAR(20)
);

CREATE TABLE Model (
   Model_Id        VARCHAR2(5) PRIMARY KEY,
   Model_Name      VARCHAR(20),
   Manufacturer_Id INTEGER,
   Nickname        VARCHAR(20),
   Capacity        INTEGER,
   Range           INTEGER,
   Cruising_Speed  INTEGER,
   Engine_Type     VARCHAR(30),
   CONSTRAINT Model_References_Manufacturer FOREIGN KEY ( Manufacturer_Id )
      REFERENCES Manufacturer ( Man_Id )
);

CREATE TABLE Airplane (
   Regno        VARCHAR(10) PRIMARY KEY,
   Model_Id     VARCHAR2(5),
   First_Flight DATE,
   CONSTRAINT Airplane_References_Model FOREIGN KEY ( Model_Id )
      REFERENCES Model ( Model_Id )
);

CREATE TABLE Technician (
   Ssn     NUMBER(9) PRIMARY KEY,
   Name    VARCHAR(20),
   Salary  FLOAT,
   Phno    NUMBER(10),
   Address VARCHAR(50)
);

CREATE TABLE Technician_Expertise (
   Tech_Ssn            NUMBER(9),
   Airplane_Model      VARCHAR2(20),
   Years_Of_Experience NUMBER(4),
   CONSTRAINT Expertise_References_Model FOREIGN KEY ( Airplane_Model )
      REFERENCES Model ( Model_Id ),
   CONSTRAINT Expertise_References_Technician FOREIGN KEY ( Tech_Ssn )
      REFERENCES Technician ( Ssn )
);

-- ALTER TABLE Technician_Expertise ADD Years_Of_Experience NUMBER(4);
-- UPDATE TECHNICIAN_EXPERTISE
--    SET
--    YEARS_OF_EXPERIENCE = 5;


CREATE TABLE Test (
   Test_Id          VARCHAR(4) PRIMARY KEY,
   Test_Name        VARCHAR(30),
   Test_Description VARCHAR(150),
   Test_Periodicity INTEGER, -- REPRESENTS MONTHS
   Test_Max_Score   INTEGER
);

CREATE TABLE Test_Info (
   TestInfo_ID   VARCHAR(10),
   Test_Id       VARCHAR(4)   NOT NULL,
   Airpl_Regno   VARCHAR(10)  NOT NULL,
   Tech_Ssn      NUMBER(9)    NOT NULL,
   Proposed_Date DATE         NOT NULL,
   Actual_Date   DATE,
   Hours         INTEGER      NOT NULL,
   Score         INTEGER      NOT NULL,
   CONSTRAINT Test_Info_References_Test FOREIGN KEY ( Test_Id )
      REFERENCES Test ( Test_Id ),
   CONSTRAINT Test_Info_References_Airplane FOREIGN KEY ( Airpl_Regno )
      REFERENCES Airplane ( Regno ),
   CONSTRAINT Test_Info_References_Technician FOREIGN KEY ( Tech_Ssn )
      REFERENCES Technician ( Ssn )
);

CREATE SEQUENCE Model_Id_Seq START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE TestInfo_Id_Seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE OR REPLACE TRIGGER Model_Id_Generator BEFORE
   INSERT ON Model
   FOR EACH ROW
BEGIN
   IF :New.Model_Id IS NULL THEN
      :New.Model_Id := Concat(
         'M0',
         Model_Id_Seq.Nextval
      );
   END IF;
END;
/
CREATE OR REPLACE TRIGGER TestInfo_Id_Generator BEFORE
   INSERT ON Test_Info
   FOR EACH ROW
BEGIN
   IF :New.TestInfo_ID IS NULL THEN
      :New.TestInfo_ID := Concat(
         'Ti0',
         TestInfo_Id_Seq.Nextval
      );
   END IF;
END;
/

-- -- Allow insertion of values into database
-- ALTER USER Pranav
--    QUOTA 200M ON Users;


-- INSERTION OF VALUES
@"./data.sql"

-- SAVE ALL CHANGES
COMMIT;

-- TESTING

-- SELECT DISTINCT Airpl_Regno
--   FROM Test_Info;

-- SELECT *
--   FROM MANUFACTURER;

-- var c refcursor
-- exec usp_GetAllManufacturers(:c)
-- print c

