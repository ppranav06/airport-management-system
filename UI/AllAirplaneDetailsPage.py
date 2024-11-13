import customtkinter as ctk
import PIL
from BAL import Airplanes
from Images.Images import Images

from DATA.Data import Data

# ModelData=Data.Models
# AirplaneData=Data.Airplanes

airplanes=Airplanes.Airplanes()
images=Images()
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


        self.canvas=ctk.CTkCanvas(self,width=250,height=1000)
        self.canvas.pack(fill='both')
        self.bgLabel=ctk.CTkLabel(self.canvas,text='',image=ctk.CTkImage(light_image=PIL.Image.open(r'Images\SideFrameBg.png'),size=(250,700)))
        self.bgLabel.place(x=0,y=0)

        self.btnHome=ctk.CTkButton(self.canvas,text='Home',bg_color='#2596BE',command=self.master.master.LoadHomePage)
        self.btnHome.place(y=670,x=55)

        self.btnBack=ctk.CTkButton(self.canvas,text='Back',bg_color='#2596be',command=self.master.master.LoadHomePage)
        self.btnBack.place(y=640,x=55)
        
        
class AllAirplanesFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1150,fg_color='white')
        
        self.grid_columnconfigure((0,1,2),weight=1)
        # self.grid_rowconfigure(0,weight=1)
        # self.grid_rowconfigure(1,weight=1)
        # self.grid_rowconfigure(2,weight=10)

        self.manufactureresFrame=ManufacturersFrame(self)
        self.manufactureresFrame.grid(column=0,row=2,sticky='we',padx=20,pady=20)

        self.modelsPlaceHolderFrame=ModelsPlaceHolderFrame(self)
        self.modelsPlaceHolderFrame.grid(column=1,row=2,sticky='we',padx=20,pady=20)

        self.airplanesPlaceHolderFrame=AirplanesPlaceHolderFrame(self)
        self.airplanesPlaceHolderFrame.grid(column=2,row=2,sticky='we',padx=20,pady=20)

        self.lblManufacturers=ctk.CTkLabel(self,text='Manufacturers',font=ctk.CTkFont(size=20,weight='bold',family='Kode Mono'),text_color='white',height=60,
                                           image=ctk.CTkImage(light_image=PIL.Image.open(r'Images\ManufacturersHeading.png'),size=(400,70)))
        self.lblModels=ctk.CTkLabel(self,text='Models',font=ctk.CTkFont(size=20,weight='bold',family='Kode Mono'),text_color='white',height=60,
                                           image=ctk.CTkImage(light_image=PIL.Image.open(r'Images\ModelsHeading.png'),size=(400,70)))
        self.lblAirplanes=ctk.CTkLabel(self,text='Airplane Registration No',font=ctk.CTkFont(size=20,weight='bold',family='Kode Mono'),text_color='white',height=60,
                                           image=ctk.CTkImage(light_image=PIL.Image.open(r'Images\AirplanesHeading.png'),size=(400,70)))

        self.lblManufacturers.grid(row=0,column=0,pady=5,padx=10,sticky='news')
        self.lblModels.grid(row=0,column=1,pady=5,padx=10,sticky='news')
        self.lblAirplanes.grid(row=0,column=2,pady=5,padx=10,sticky='news')

        self.SelectedManufacturer=ctk.StringVar(value='')
        self.SelectedModel=ctk.StringVar(value='')

        self.lblSelectedManufacturerVal=ctk.CTkLabel(self,textvariable=self.SelectedManufacturer,font=ctk.CTkFont(size=15,slant='italic'))
        self.lblSelectedModelVal=ctk.CTkLabel(self,textvariable=self.SelectedModel,font=ctk.CTkFont(size=15,slant='italic'))


        self.lblSelectedManufacturerVal.grid(row=1,column=1,padx=5)
        self.lblSelectedModelVal.grid(row=1,column=2,padx=5)





class ManufacturersFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=560,width=380,fg_color='white')
         
        # ManufacturerImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\6131.webp'),size=(250,150))
        for manufacturerID,manufacturerName in airplanes.GetAllManufacturers():
            ManufacturerImage=ctk.CTkImage(light_image=images.ManufacturerImages[manufacturerName],size=(250,150))
            btn=ctk.CTkButton(self,image=ManufacturerImage,
                              text=manufacturerName,
                              command=lambda i=manufacturerID,m=manufacturerName:self.SelectNewManufacturer(i,m),
                              fg_color='transparent',
                              text_color='black',
                              corner_radius=3,
                              compound='top',
                              hover_color='lightgrey')
            btn.pack(pady=20,padx=30,fill='x')

    def SelectNewManufacturer(self,manufacturerID,manufacturerName):
        target=self.master.master.master.modelsPlaceHolderFrame
        if target.modelsFrame!=None:
            target.modelsFrame.destroy()
        self.master.master.master.SelectedManufacturer.set('SELECTED MANUFACTURER: '+str(manufacturerName))
        target.modelsFrame=ModelsFrame(target,manufacturerID)
        target.modelsFrame.pack()
        
        

class ModelsPlaceHolderFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=560,width=380)

        self.modelsFrame=None

class AirplanesPlaceHolderFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=560,width=380)
        self.airplanesFrame=None
class ModelsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,manufacturerID, **kwargs):
        super().__init__(master, **kwargs,height=560,width=380,fg_color='white')
        for modelData in airplanes.GetModels(manufacturerID):
            ModelImage=ctk.CTkImage(light_image=images.ModelImages[modelData[1]],size=(300,200))
            btn=ctk.CTkButton(self,
                                image=ModelImage,
                                text=modelData[1],
                                command=lambda i=modelData[0],m=modelData[1]:self.SelectNewModel(i,m),
                                fg_color='transparent',
                                compound='top',
                                text_color='black',
                                hover_color='lightgrey')
            btn.pack()

    def SelectNewModel(self,modelID,modelName):
        target=self.master.master.master.master.airplanesPlaceHolderFrame
        if target.airplanesFrame!=None:
            target.airplanesFrame.destroy()
        self.master.master.master.master.SelectedModel.set('SELECTED MODEL: '+modelName)
        target.airplanesFrame=AirplanesFrame(target,modelID)
        target.airplanesFrame.pack()

    def destroy(self):
        target=self.master.master.master.master.airplanesPlaceHolderFrame
        if target.airplanesFrame!=None:
            target.airplanesFrame.destroy()
        self.master.master.master.master.SelectedManufacturer.set('')
        self.pack_forget()
 
class AirplanesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,modelID, **kwargs):
        super().__init__(master, **kwargs,height=560,width=380,fg_color='white')
        root=self.master.master.master.master.master.master

        for aircraft in airplanes.GetAirplanes(modelID):
            if isinstance(aircraft.State,Airplanes.TestsPendingState):
                color='#cd581c'
                hoverColor='#a84817'
            if isinstance(aircraft.State,Airplanes.TestsCompleteState):
                color='#2596be'
                hoverColor='#1e7998'
            btn=ctk.CTkButton(self,text=aircraft.Details[0],command=lambda m=aircraft.Details[0]:root.LoadAirplaneDetailsPage(m),fg_color=color,hover_color=hoverColor)
            btn.pack()

    def destroy(self):
        self.master.master.master.master.SelectedModel.set('')
        self.pack_forget()


    