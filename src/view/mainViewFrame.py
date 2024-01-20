import customtkinter
from src.view import testeViewFrame
from src.view import testeNovamenteViewFrame

class MainViewFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        #FrameTeste
        self.frame_test = testeViewFrame.TestViewFrame(master=self)
        self.frame_test.grid(row=0, column=0, padx=(30,10), pady=(15, 15),sticky="nsew")
        
        #FrameTeste
        self.frameNovo_test = testeNovamenteViewFrame.TestNovamenteViewFrame(master=self)
        self.frameNovo_test.grid(row=0, column=1, padx=(10,30), pady=(15, 15),sticky="wnse")
        
        
        self.back_button = customtkinter.CTkButton(self, text="Teste")
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15),stick="wse",columnspan=2)
        
    
    # def back_event(self):
    #     print("Voltar")
        #self.main_frame.grid_forget()  # remove main frame
        #self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame