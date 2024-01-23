import customtkinter
from src.controller import comunicaoArduino
from src.view import configViewFrame


class TestViewFrame(customtkinter.CTkFrame):
    def __init__(self, 
                 master,
                 comunicacaoArduino:comunicaoArduino.ComunicacaoArduino, 
                 **kwargs):
        super().__init__(master, **kwargs)
        
        self.comunica_arduino = comunicacaoArduino
        
        self.button = customtkinter.CTkButton(self,text="Open conexao",command=self.button_teste)
        self.button.grid(row=0, column=0, padx=(30,10), pady=(15, 5))
        
        self.input = customtkinter.CTkEntry(self,placeholder_text="Envidar dados arduino")
        self.input.grid(row=1, column=0, padx=(30,10), pady=(15, 5))
        
        self.buttonEnv = customtkinter.CTkButton(self,text="Enviadar dados",command=self.button_env)
        self.buttonEnv.grid(row=2, column=0, padx=(30,10), pady=(15, 5))
        
        self.buttonRec = customtkinter.CTkButton(self,text="Receber dados",command=self.button_rec)
        self.buttonRec.grid(row=3, column=0, padx=(30,10), pady=(15, 5))
        
        self.buttonFechar = customtkinter.CTkButton(self,text="Fechar conexão",command=self.button_fechar)
        self.buttonFechar.grid(row=4, column=0, padx=(30,10), pady=(15, 5))
        
        
        self.textbox = customtkinter.CTkTextbox(master=self, width=600, corner_radius=0)
        self.textbox.grid(row=5, column=0, sticky="nsew")
        
        
        
    def button_teste(self):
        self.comunica_arduino.open_connection()
        
    def button_env(self):
        self.comunica_arduino.send_data(self.input.get())
        self.textbox.insert("0.0", self.comunica_arduino.read_data())
        
    def button_rec(self):
        self.comunica_arduino.read_data()
        
    def button_fechar(self):
        self.comunica_arduino.close_connection()
        
        
        
        