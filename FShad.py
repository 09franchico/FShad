import customtkinter
from PIL import Image
import os
from src.view import loginViewFrame
from src.controller import comunicaoArduino
from src.controller import coreController

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600
    x = 500
    y = 200

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("FShad")
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.resizable(False, False)
        
         # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(
            Image.open(current_path + "/src/images/bg_gradient.jpg"),
            size=(self.width, self.height))
        
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        
        self.comunicacao_arduino_instance = comunicaoArduino.ComunicacaoArduino("COM5")
        
        #Model
        
        
        
        #LoginFrame  View  
        self.login_frame = loginViewFrame.LoginViewFrame(
            master = self,
            comunicacaoArduino = self.comunicacao_arduino_instance)
        self.login_frame.grid(row=0, column=0,sticky="ns")
        
        # Criar o controlador
        controller = coreController.Controller(arduino=self.comunicacao_arduino_instance, views=self.login_frame)
        self.login_frame.main_frame.frame_test.set_controller(controller)
        self.login_frame.main_frame.frameNovo_test.set_controller(controller)
        
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()