import customtkinter
import tkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("src/theme/theme.json")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("FShad")
        self.geometry("1000x500+450+250")
        self.grid_columnconfigure((0, 1), weight=1)
        
        self.txt_logs = tkinter.Text(
            bg="#0E0E0D",
            fg="#5AE05E",
        )
        self.txt_logs.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.txt_logs.insert(tkinter.END,"Ola munod")
        
        
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()