import PIL,os

cwd = os.getcwd()

class Images:
    _ManufacturerImageLocations={'Boeing':'6131.webp','Airbus':'AirbusLogo.png','Piper':'PiperLogo.jpg','Cirrus':'CirrusLogo.png','Cessna':'CessnaLogo.jpg'}
    _ModelImageLocations={'787':'787.jpg','777':'777.jpg','747':'747.jpg','737':'737.jpg','A380':'A380.jpg','A350':'A350.jpg','A320':'A320.jpg','SR22':'SR22.jpg','PA-28 Warrior':'PA22Warrior.jpg','172 Skyhawk':'172SkyHawk.jpg'}
    ManufacturerImages={name:PIL.Image.open(os.path.join(cwd,'Images',location)) for name,location in _ManufacturerImageLocations.items()}
    ModelImages={name:PIL.Image.open(os.path.join(cwd,'Images',location)) for name,location in _ModelImageLocations.items()}
    