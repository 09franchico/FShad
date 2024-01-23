import customtkinter

from src.controller import comunicaoArduino

class ConfigViewFrame(customtkinter.CTkFrame):
    def __init__(self, 
                 master,
                 comunicacao_arduino:comunicaoArduino.ComunicacaoArduino, **kwargs):
        super().__init__(master, **kwargs)
         
        # self.comunicacaoAr = comunicacao_arduino;
        # self.textbox = customtkinter.CTkTextbox(master=self, width=100, corner_radius=0,text_color="green")
        # self.textbox.grid(row=0, column=0, sticky="nsew")
    
        
    #     self.buttonFechar = customtkinter.CTkButton(self,text="Teste",command=self.button_teste)
    #     self.buttonFechar.grid(row=1, column=0, padx=(30,10), pady=(15, 5))
        
    # def button_teste(self):
    #     self.comunicacaoAr.send_data("teste")
    #     self.textbox.insert("0.0",self.comunicacaoAr.read_data())
        