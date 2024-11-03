import customtkinter as ctk
import PIL

from DATA.Data import Data

AirplaneData=Data.Airplanes

class AllAirplanePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        lbl_AirplaneRecords=ctk.CTkLabel(master=self,text='Airplane Records',font=ctk.CTkFont(size=50))
        lbl_AirplaneRecords.pack()

        for i in range(3):
            self.scrollable1=AirplaneCategoryScrollable(master=self,height=200,width=1300,border_width=0,orientation='horizontal')
            self.scrollable1.pack()


class AirplaneCategoryScrollable(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        for i in range(6):
            b1=AirplaneTile(master=self)
            b1.pack(side=ctk.LEFT)


class AirplaneTile(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        airplaneImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\Airplane1.jpeg'),size=(200,200))
        super().__init__(master, **kwargs,
                         text="Airplane 1",
                         image=airplaneImage,
                         height=100,
                         fg_color='transparent')