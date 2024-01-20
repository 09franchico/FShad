import customtkinter


class TestViewFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        # self.grid_columnconfigure(0, weight=1)
    
        # self.back_button = customtkinter.CTkButton(self, text="Back", width=200)
        # self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15), sticky="nsew")
        
    
    # def back_event(self):
    #     print("Voltar")
        #self.main_frame.grid_forget()  # remove main frame
        #self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame