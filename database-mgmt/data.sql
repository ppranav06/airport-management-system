-- INSERTION OF VALUES FOR AMS DATABASE

-- MANUFACTURER

INSERT INTO Manufacturer VALUES ( 1,
                                  'Boeing' );
INSERT INTO Manufacturer VALUES ( 2,
                                  'Airbus' );
INSERT INTO Manufacturer VALUES ( 3,
                                  'Cirrus' );
INSERT INTO Manufacturer VALUES ( 4,
                                  'Piper' );
INSERT INTO Manufacturer VALUES ( 5,
                                  'Cessna' );

-- MODELS

INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( '747',
           1,
           'Jumbo Jet',
           416,
           8000,
           560,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( 'A380',
           2,
           'Superjumbo',
           544,
           8500,
           590,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( '777',
           1,
           'Triple Seven',
           396,
           9400,
           580,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( 'A350',
           2,
           'Extra Widebody',
           325,
           9700,
           590,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( '787',
           1,
           'Dreamliner',
           242,
           7635,
           560,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( 'A320',
           2,
           'Short-Haul Workhorse',
           180,
           3100,
           500,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( '737',
           1,
           'Short-Haul King',
           189,
           3100,
           490,
           'Turbo-fan' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( '172 Skyhawk',
           5,
           'Pilot Trainer',
           380,
           650,
           110,
           'Reciprocating' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( 'PA-28 Warrior',
           4,
           'Student Favorite',
           140,
           650,
           110,
           'Reciprocating' );
INSERT INTO Model (
   Model_Name,
   Manufacturer_Id,
   Nickname,
   Capacity,
   Range,
   Cruising_Speed,
   Engine_Type
) VALUES ( 'SR22',
           3,
           'Personal Jet',
           240,
           1100,
           175,
           'Turbocharged Reciprocating' );

SELECT *
  FROM Manufacturer;
SELECT *
  FROM Model;

-- AIRPLANE

INSERT INTO Airplane VALUES ( 'F-WWDD',
                              'M01',
                              TO_DATE('2020-01-15','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'A6-EDA',
                              'M02',
                              TO_DATE('2020-02-20','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'N123AB',
                              'M03',
                              TO_DATE('2020-03-25','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'G-AVIT',
                              'M04',
                              TO_DATE('2020-04-30','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'C-FXYZ',
                              'M05',
                              TO_DATE('2020-05-05','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'D-ABCD',
                              'M06',
                              TO_DATE('2020-06-10','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'VH-XYZ',
                              'M07',
                              TO_DATE('2020-07-15','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'JA-ABC',
                              'M08',
                              TO_DATE('2020-08-20','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'B-1234',
                              'M09',
                              TO_DATE('2020-09-25','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'OY-XYZ',
                              'M010',
                              TO_DATE('2020-10-30','YYYY-MM-DD') );

INSERT INTO Airplane VALUES ( 'F-GHJK',
                              'M01',
                              TO_DATE('2021-01-10','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'PH-DEF',
                              'M02',
                              TO_DATE('2021-02-15','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'N456CD',
                              'M03',
                              TO_DATE('2021-03-20','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'C-GHJK',
                              'M04',
                              TO_DATE('2021-04-25','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'I-XYZP',
                              'M05',
                              TO_DATE('2021-05-30','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'D-XYZY',
                              'M06',
                              TO_DATE('2021-06-05','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'EC-XYZ',
                              'M07',
                              TO_DATE('2021-07-10','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'ZK-ABC',
                              'M08',
                              TO_DATE('2021-08-15','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'TC-XYZ',
                              'M09',
                              TO_DATE('2021-09-20','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'HK-ABC',
                              'M010',
                              TO_DATE('2021-10-25','YYYY-MM-DD') );

INSERT INTO Airplane VALUES ( 'M-ABCD',
                              'M01',
                              TO_DATE('2022-01-05','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'N-XYZ',
                              'M02',
                              TO_DATE('2022-02-10','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'G-BHJK',
                              'M03',
                              TO_DATE('2022-03-15','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'F-ABCD',
                              'M04',
                              TO_DATE('2022-04-20','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'A6-BCD',
                              'M05',
                              TO_DATE('2022-05-25','YYYY-MM-DD') );
INSERT INTO Airplane VALUES ( 'D-XYZK',
                              'M06',
                              TO_DATE('2022-06-30','YYYY-MM-DD') );

-- TECHNICIAN

INSERT INTO Technician VALUES ( 123456789,
                                'Alice Johnson',
                                55000.00,
                                9876543210,
                                '123 Elm St, Springfield' );
INSERT INTO Technician VALUES ( 234567890,
                                'Bob Sundareswaran',
                                62000.00,
                                8765432109,
                                '456 Oak St, Lincoln' );
INSERT INTO Technician VALUES ( 345678901,
                                'Charlie Brown',
                                58000.00,
                                7654321098,
                                '789 Pine St, Maplewood' );
INSERT INTO Technician VALUES ( 456789012,
                                'Dana White',
                                60000.00,
                                6543210987,
                                '101 Cedar St, Rivertown' );
INSERT INTO Technician VALUES ( 567890123,
                                'Eve Davis',
                                57000.00,
                                5432109876,
                                '202 Birch St, Hilltop' );
INSERT INTO Technician VALUES ( 678901234,
                                'Frank Green',
                                64000.00,
                                4321098765,
                                '303 Maple St, Lakeview' );
INSERT INTO Technician VALUES ( 789012345,
                                'Grace Lee',
                                65000.00,
                                3210987654,
                                '404 Willow St, Oakwood' );
INSERT INTO Technician VALUES ( 890123456,
                                'Henry King',
                                59000.00,
                                2109876543,
                                '505 Cherry St, Brookside' );
INSERT INTO Technician VALUES ( 901234567,
                                'Will Turner',
                                63000.00,
                                1098765432,
                                '606 Walnut St, Eastwood' );
INSERT INTO Technician VALUES ( 112345678,
                                'Jack Wilson',
                                62000.00,
                                1987654321,
                                '707 Ash St, Westfield' );

INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 123456789,
           'M01',
           1 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 123456789,
           'M02',
           1 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 234567890,
           'M09',
           2 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 234567890,
           'M04',
           1 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 345678901,
           'M05',
           2 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 345678901,
           'M06',
           5 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 456789012,
           'M07',
           6 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 456789012,
           'M07',
           2 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 567890123,
           'M09',
           4 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 567890123,
           'M01',
           2 );

INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 678901234,
           'M01',
           3 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 678901234,
           'M02',
           3 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 789012345,
           'M03',
           5 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 789012345,
           'M04',
           4 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 890123456,
           'M03',
           1 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 890123456,
           'M06',
           6 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 901234567,
           'M05',
           7 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 901234567,
           'M08',
           1 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 112345678,
           'M09',
           2 );
INSERT INTO Technician_Expertise (
   TECH_SSN,
   AIRPLANE_MODEL,
   Years_Of_Experience
) VALUES ( 112345678,
           'M010',
           1 );

SELECT *
  FROM Technician_Expertise;

-- TEST

INSERT INTO Test VALUES ( 'T001',
                          'Pre-Flight',
                          'Test conducted before flight to ensure aircraft readiness',
                          12,
                          100 );
INSERT INTO Test VALUES ( 'T002',
                          'Post-Flight',
                          'Assessment after flight to evaluate performance and any issues',
                          12,
                          100 );
INSERT INTO Test VALUES ( 'T003',
                          'Engine Check',
                          'Regular checks on engine performance and safety',
                          6,
                          50 );
INSERT INTO Test VALUES ( 'T004',
                          'Safety Inspection',
                          'Comprehensive safety checks of all systems',
                          12,
                          100 );
INSERT INTO Test VALUES ( 'T005',
                          'Turbulence Test',
                          'Evaluation of aircraft performance in turbulent conditions',
                          24,
                          75 );
INSERT INTO Test VALUES ( 'T006',
                          'Landing Gear Check',
                          'Assessment of landing gear functionality and safety',
                          12,
                          50 );
INSERT INTO Test VALUES ( 'T007',
                          'Avionics Check',
                          'Testing of all avionics systems for proper operation',
                          6,
                          80 );
INSERT INTO Test VALUES ( 'T008',
                          'Fuel System Test',
                          'Check and evaluation of fuel systems for leaks and performance',
                          12,
                          100 );
INSERT INTO Test VALUES ( 'T009',
                          'Emergency Systems Test',
                          'Evaluation of emergency systems functionality',
                          12,
                          100 );
INSERT INTO Test VALUES ( 'T010',
                          'Cabin Safety Review',
                          'Inspection of cabin safety equipment and protocols',
                          12,
                          100 );

-- TEST_INFO

INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T001',
           'F-WWDD',
           123456789,
           TO_DATE('2023-01-10','YYYY-MM-DD'),
           TO_DATE('2023-01-15','YYYY-MM-DD'),
           5,
           90 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T002',
           'F-WWDD',
           123456789,
           TO_DATE('2024-01-10','YYYY-MM-DD'),
           TO_DATE('2024-01-13','YYYY-MM-DD'),
           6,
           100 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T003',
           'F-WWDD',
           123456789,
           TO_DATE('2024-01-10','YYYY-MM-DD'),
           TO_DATE('2024-01-15','YYYY-MM-DD'),
           7,
           40 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T004',
           'F-WWDD',
           123456789,
           TO_DATE('2024-01-10','YYYY-MM-DD'),
           TO_DATE('2024-01-15','YYYY-MM-DD'),
           9,
           75 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T002',
           'A6-EDA',
           234567890,
           TO_DATE('2023-02-20','YYYY-MM-DD'),
           TO_DATE('2023-02-25','YYYY-MM-DD'),
           4,
           95 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T003',
           'N123AB',
           345678901,
           TO_DATE('2023-03-15','YYYY-MM-DD'),
           TO_DATE('2023-03-20','YYYY-MM-DD'),
           3,
           45 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T004',
           'G-AVIT',
           456789012,
           TO_DATE('2023-04-10','YYYY-MM-DD'),
           TO_DATE('2023-04-15','YYYY-MM-DD'),
           2,
           85 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T005',
           'C-FXYZ',
           567890123,
           TO_DATE('2023-05-05','YYYY-MM-DD'),
           TO_DATE('2023-05-10','YYYY-MM-DD'),
           6,
           70 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T006',
           'D-ABCD',
           678901234,
           TO_DATE('2023-06-01','YYYY-MM-DD'),
           TO_DATE('2023-06-05','YYYY-MM-DD'),
           4,
           42 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T007',
           'VH-XYZ',
           789012345,
           TO_DATE('2023-07-10','YYYY-MM-DD'),
           TO_DATE('2023-07-15','YYYY-MM-DD'),
           3,
           78 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T008',
           'JA-ABC',
           890123456,
           TO_DATE('2023-08-20','YYYY-MM-DD'),
           TO_DATE('2023-08-25','YYYY-MM-DD'),
           5,
           75 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T009',
           'B-1234',
           901234567,
           TO_DATE('2023-09-15','YYYY-MM-DD'),
           TO_DATE('2023-09-20','YYYY-MM-DD'),
           2,
           90 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T010',
           'OY-XYZ',
           112345678,
           TO_DATE('2023-10-10','YYYY-MM-DD'),
           TO_DATE('2023-10-15','YYYY-MM-DD'),
           4,
           87 );

INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T001',
           'F-GHJK',
           123456789,
           TO_DATE('2023-01-15','YYYY-MM-DD'),
           TO_DATE('2023-01-20','YYYY-MM-DD'),
           5,
           92 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T006',
           'F-GHJK',
           123456789,
           TO_DATE('2023-01-15','YYYY-MM-DD'),
           TO_DATE('2023-01-20','YYYY-MM-DD'),
           5,
           48 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T007',
           'F-GHJK',
           123456789,
           TO_DATE('2023-01-15','YYYY-MM-DD'),
           TO_DATE('2023-01-20','YYYY-MM-DD'),
           5,
           62 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T009',
           'F-GHJK',
           123456789,
           TO_DATE('2023-01-15','YYYY-MM-DD'),
           TO_DATE('2023-01-20','YYYY-MM-DD'),
           5,
           92 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T002',
           'PH-DEF',
           234567890,
           TO_DATE('2023-02-25','YYYY-MM-DD'),
           TO_DATE('2023-03-02','YYYY-MM-DD'),
           4,
           94 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T003',
           'N456CD',
           345678901,
           TO_DATE('2023-03-20','YYYY-MM-DD'),
           TO_DATE('2023-03-25','YYYY-MM-DD'),
           3,
           50 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T004',
           'C-GHJK',
           456789012,
           TO_DATE('2023-04-15','YYYY-MM-DD'),
           TO_DATE('2023-04-20','YYYY-MM-DD'),
           2,
           86 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T005',
           'I-XYZP',
           567890123,
           TO_DATE('2023-05-10','YYYY-MM-DD'),
           TO_DATE('2023-05-15','YYYY-MM-DD'),
           6,
           75 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T006',
           'D-XYZY',
           678901234,
           TO_DATE('2023-06-05','YYYY-MM-DD'),
           TO_DATE('2023-06-10','YYYY-MM-DD'),
           4,
           41 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T007',
           'EC-XYZ',
           789012345,
           TO_DATE('2023-07-15','YYYY-MM-DD'),
           TO_DATE('2023-07-20','YYYY-MM-DD'),
           3,
           59 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T008',
           'ZK-ABC',
           890123456,
           TO_DATE('2023-08-25','YYYY-MM-DD'),
           TO_DATE('2023-08-30','YYYY-MM-DD'),
           5,
           76 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T009',
           'TC-XYZ',
           901234567,
           TO_DATE('2023-09-20','YYYY-MM-DD'),
           TO_DATE('2023-09-25','YYYY-MM-DD'),
           2,
           91 );
INSERT INTO Test_Info (
   Test_Id,
   Airpl_Regno,
   Tech_Ssn,
   Proposed_Date,
   Actual_Date,
   Hours,
   Score
) VALUES ( 'T010',
           'HK-ABC',
           112345678,
           TO_DATE('2023-10-15','YYYY-MM-DD'),
           TO_DATE('2023-10-20','YYYY-MM-DD'),
           4,
           84 );

-- SAVE CHANGES
COMMIT;