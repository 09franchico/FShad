import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("FShad")
        self.geometry("1000x500+450+250")
        self.grid_columnconfigure((0, 1), weight=1)
        
        
        

        
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()