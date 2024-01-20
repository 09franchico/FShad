import customtkinter
from PIL import Image
import os
from src.view import loginViewFrame

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
        
        #LoginFrame    
        self.login_frame = loginViewFrame.LoginViewFrame(master=self)
        self.login_frame.grid(row=0, column=0,sticky="ns")


if __name__ == "__main__":
    app = App()
    app.mainloop()