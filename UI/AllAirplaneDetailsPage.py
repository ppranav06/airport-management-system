import customtkinter as ctk
import PIL

from DATA.Data import Data

ModelData=Data.Models
AirplaneData=Data.Airplanes

class AllAirplanesPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)

        
        self.technicianSideFrame=SideFrame(self)
        self.technicianSideFrame.pack(side=ctk.LEFT)
        self.technicianSideFrame.pack_propagate(0)

        self.allAirplanesFrame=AllAirplanesFrame(self)
        self.allAirplanesFrame.pack(side=ctk.LEFT,fill='x')
        
class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=250)

        self.btnHome=ctk.CTkButton(self,text='Home',command=self.master.master.LoadHomePage)
        self.btnHome.pack(side=ctk.BOTTOM)
        
class AllAirplanesFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1150,fg_color='white')
        
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=10)

        self.manufactureresFrame=ManufacturersFrame(self)
        self.manufactureresFrame.grid(column=0,row=2,sticky='we',padx=20,pady=20)

        self.modelsPlaceHolderFrame=ModelsPlaceHolderFrame(self)
        self.modelsPlaceHolderFrame.grid(column=1,row=2,sticky='we',padx=20,pady=20)

        self.airplanesPlaceHolderFrame=AirplanesPlaceHolderFrame(self)
        self.airplanesPlaceHolderFrame.grid(column=2,row=2,sticky='we',padx=20,pady=20)

        self.lblManufacturers=ctk.CTkLabel(self,text='MANUFACTURER',font=ctk.CTkFont(size=20,weight='bold'))
        self.lblModels=ctk.CTkLabel(self,text='MODELS',font=ctk.CTkFont(size=20,weight='bold'))
        self.lblAirplanes=ctk.CTkLabel(self,text='AIRPLANE REGISTRATION NO',font=ctk.CTkFont(size=20,weight='bold'))

        self.lblManufacturers.grid(row=0,column=0,pady=20)
        self.lblModels.grid(row=0,column=1,pady=20)
        self.lblAirplanes.grid(row=0,column=2,pady=20)

        self.SelectedManufacturer=ctk.StringVar(value='')
        self.SelectedModel=ctk.StringVar(value='')

        self.lblSelectedManufacturerVal=ctk.CTkLabel(self,textvariable=self.SelectedManufacturer,font=ctk.CTkFont(size=15,slant='italic'))
        self.lblSelectedModelVal=ctk.CTkLabel(self,textvariable=self.SelectedModel,font=ctk.CTkFont(size=15,slant='italic'))


        self.lblSelectedManufacturerVal.grid(row=1,column=1,padx=5)
        self.lblSelectedModelVal.grid(row=1,column=2,padx=5)





class ManufacturersFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=380,fg_color='white')
         
        ManufacturerImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\6131.webp'),size=(250,150))
        for manufacturer in ['Boeing','Airbus','Cirrus','Piper','Cessna']:
            btn=ctk.CTkButton(self,image=ManufacturerImage,
                              text=manufacturer,
                              command=lambda m=manufacturer:self.SelectNewManufacturer(m),
                              fg_color='transparent',
                              text_color='black',
                              corner_radius=3,
                              compound='top',
                              hover_color='lightgrey')
            btn.pack(pady=20,padx=30,fill='x')

    def SelectNewManufacturer(self,manufacturer):
        target=self.master.master.master.modelsPlaceHolderFrame
        if target.modelsFrame!=None:
            target.modelsFrame.destroy()
        self.master.master.master.SelectedManufacturer.set('SELECTED MANUFACTURER: '+manufacturer)
        target.modelsFrame=ModelsFrame(target,manufacturer)
        target.modelsFrame.pack()
        
        

class ModelsPlaceHolderFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=380)

        self.modelsFrame=None

class AirplanesPlaceHolderFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=380)

        self.airplanesFrame=None
class ModelsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,manufacturer, **kwargs):
        super().__init__(master, **kwargs,height=700,width=380,fg_color='white')
        ModelImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\737.jpeg'),size=(250,200))
        for model in ModelData.values():
            if model["Manufacturer"].lower()==manufacturer.lower():
                btn=ctk.CTkButton(self,
                                  image=ModelImage,
                                  text=model["Model"],
                                  command=lambda m=model["Model"]:self.SelectNewModel(m),
                                  fg_color='transparent',
                                  compound='top',
                                  text_color='black',
                                  hover_color='lightgrey')
                btn.pack()

    def SelectNewModel(self,model):
        target=self.master.master.master.master.airplanesPlaceHolderFrame
        if target.airplanesFrame!=None:
            target.airplanesFrame.destroy()
        self.master.master.master.master.SelectedModel.set('SELECTED MODEL: '+model)
        target.airplanesFrame=AirplanesFrame(target,model)
        target.airplanesFrame.pack()

    def destroy(self):
        target=self.master.master.master.master.airplanesPlaceHolderFrame
        if target.airplanesFrame!=None:
            target.airplanesFrame.destroy()
        self.master.master.master.master.SelectedManufacturer.set('')
        self.pack_forget()
 
class AirplanesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,model, **kwargs):
        super().__init__(master, **kwargs,height=700,width=380)
        root=self.master.master.master.master.master.master
        print(root)

        for registrationNo,airplane in AirplaneData.items():
            if airplane["Model"].lower()==model.lower():
                btn=ctk.CTkButton(self,text=registrationNo,command=lambda m=registrationNo:root.LoadAirplaneDetailsPage(m))
                btn.pack()

    def destroy(self):
        self.master.master.master.master.SelectedModel.set('')
        self.pack_forget()


    