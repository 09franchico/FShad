import customtkinter

from src.controller import comunicaoArduino

class ConfigViewFrame(customtkinter.CTkFrame):
    def __init__(self, 
                 master,
                 comunicacao_arduino:comunicaoArduino.ComunicacaoArduino, **kwargs):
        super().__init__(master, **kwargs)
         
        self.comunicacaoAr = comunicacao_arduino;
        self.dado = ""
        self.textbox = customtkinter.CTkTextbox(master=self, width=600, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0",self.dado)
        
    def dados_arduino(self):
        self.dado = self.comunicacaoAr.texto
        