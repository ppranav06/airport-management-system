import customtkinter as ctk
import PIL

class HomePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400)

        BgImage=ctk.CTkImage(light_image=PIL.Image.open(r'Images\AMSProjectHomePageImage.png'),size=(1400,700))
        self.bgImageCanvas=BackgroundImage(self,BgImage)
        self.bgImageCanvas.place(x=0,y=0)

        buttonFont=ctk.CTkFont(size=20,family='Eras Light ITC')
        # buttonFont=ctk.CTkFont(size=16,family='Tahoma')

        self.btnAircrafts=ctk.CTkButton(self,
                                        text='Aircrafts',
                                        fg_color='#A47239',
                                        text_color='white',
                                        corner_radius=1,
                                        hover_color='grey',
                                        font=buttonFont,
                                        command=self.master.LoadAllAirplanesPage)
        
        self.btnSingleTechnician=ctk.CTkButton(self,
                                        text='123456789',
                                        fg_color='#9E431F',
                                        text_color='white',
                                        corner_radius=1,
                                        hover_color='grey',
                                        font=buttonFont,
                                        command=lambda:self.master.LoadTechnicianDetailsPage(123456789))
        
        self.btnTechnicians=ctk.CTkButton(self,
                                        text='Technicians',
                                        fg_color='#9E431F',
                                        text_color='white',
                                        corner_radius=1,
                                        hover_color='grey',
                                        font=buttonFont,
                                        command=lambda:self.master.LoadAllTechnicianDetailsPage())

        self.btnTests=ctk.CTkButton(self,
                                        text='Test',
                                        fg_color='#4A1B26',
                                        text_color='white',
                                        corner_radius=1,
                                        hover_color='grey',
                                        font=buttonFont,
                                        command=lambda:self.master.LoadTestsPage())

        self.btnAircrafts.place(x=1080,y=400)
        self.btnTechnicians.place(x=1080,y=440) # trying to add all the technicians (can replace later)
        self.btnTests.place(x=1080,y=480)
        # self.btnSingleTechnician.place(x=1080,y=520) # can be removed

class BackgroundImage(ctk.CTkLabel):
    def __init__(self, master,bgImage, **kwargs):
        super().__init__(master, **kwargs,height=700,width=1400,image=bgImage,text='')


        