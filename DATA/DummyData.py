class Data:
    _Manufacturers={1:'Boeing',2:'Airbus',3:'Cirrus',4:'Piper',5:'Cessna'}
    _Models={
    1: {
        "Manufacturer": 1,
        "Model": "747",
        "Nickname": "Jumbo Jet",
        "Capacity": 416 ,
        "Range": 8000,
        "Cruising Speed": 560,
        "Engine Type": "Turbo-fan",
        "First Flight": "February 9, 1969"
    },
    2: {
        "Manufacturer": 2,
        "Model": "A380",
        "Nickname": "Superjumbo",
        "Capacity": 544 ,
        "Range": 8500,
        "Cruising Speed": 590,
        "Engine Type": "Turbo-fan",
        "First Flight": "April 27, 2005"
    },
    3: {
        "Manufacturer": 1,
        "Model": "777",
        "Nickname": "Triple Seven",
        "Capacity": 396 ,
        "Range": 9400,
        "Cruising Speed": 580,
        "Engine Type": "Turbo-fan",
        "First Flight": "June 12, 1994"
    },
    4: {
        "Manufacturer": 2,
        "Model": "A350",
        "Nickname": "Extra Widebody",
        "Capacity": 325 ,
        "Range": 9700,
        "Cruising Speed": 590,
        "Engine Type": "Turbo-fan",
        "First Flight": "June 14, 2013"
    },
    5: {
        "Manufacturer": 1,
        "Model": "787",
        "Nickname": "Dreamliner",
        "Capacity": 242 ,
        "Range": 7635,
        "Cruising Speed": 560,
        "Engine Type": "Turbo-fan",
        "First Flight": "December 15, 2009"
    },
    6: {
        "Manufacturer": 2,
        "Model": "A320",
        "Nickname": "Short-Haul Workhorse",
        "Capacity": 180 ,
        "Range": 3100,
        "Cruising Speed": 500,
        "Engine Type": "Turbo-fan",
        "First Flight": "February 22, 1987"
    },
    7: {
        "Manufacturer": 1,
        "Model": "737",
        "Nickname": "Short-Haul King",
        "Capacity": 189 ,
        "Range": 3100,
        "Cruising Speed": 490,
        "Engine Type": "Turbo-fan",
        "First Flight": "April 9, 1967"
    },
    8: {
        "Manufacturer": 5,
        "Model": "172 Skyhawk",
        "Nickname": "Pilot Trainer",
        "Capacity": 4 ,
        "Range": 650,
        "Cruising Speed": 110,
        "Engine Type": "Reciprocating",
        "First Flight": "June 18, 1955"
    },
    9: {
        "Manufacturer": 4,
        "Model": "PA-28 Warrior",
        "Nickname": "Student Favorite",
        "Capacity": 4 ,
        "Range": 650,
        "Cruising Speed": 110,
        "Engine Type": "Reciprocating",
        "First Flight": "December 12, 1961"
    },
    10: {
        "Manufacturer": 3,
        "Model": "SR22",
        "Nickname": "Personal Jet",
        "Capacity": 4 ,
        "Range": 1100,
        "Cruising Speed": 175,
        "Engine Type": "Turbocharged Reciprocating",
        "First Flight": "March 1998"
    }
}
    _AirCrafts={
  "N146UA": {
    "Model": 1
  },
  "G-CIVY": {
    "Model": 1
  },
  "A6-EDA": {
    "Model": 2
  },
  "F-WWDD": {
    "Model": 2
  },
  "N777UA": {
    "Model": 3
  },
  "B-2429": {
    "Model": 3
  },
  "F-WWCB": {
    "Model": 4
  },
  "A7-APA": {
    "Model": 4
  },
  "JA801A": {
    "Model": 5
  },
  "N787BA": {
    "Model": 5
  },
  "F-WWSH": {
    "Model": 6
  },
  "B-1827": {
    "Model": 6
  },
  "N737100": {
    "Model": 7
  },
  "B-1791": {
    "Model": 7
  },
  "N12345": {
    "Model": 8
  },
  "N67890": {
    "Model": 8
  },
  "N43210": {
    "Model": 9
  },
  "N98765": {
    "Model": 9
  },
  "N54321": {
    "Model": 10
  },
  "N87654": {
    "Model": 10
  }
}   
    def getAllManufacturers(self):
        return Data._Manufacturers
    
    def getModels(self,manufacturer):
        manufacturerID=[ID for ID,Name in Data._Manufacturers.items() if Name.lower()==manufacturer.lower()][0]
        return {ID:modelDetails for ID,modelDetails in Data._Models.items() if modelDetails['Manufacturer']==manufacturerID}
    
    def getAircrafts(self,model):
        pass