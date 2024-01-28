import customtkinter
from src.controller import comunicaoArduino
from src.controller import coreController
import time
import threading


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
        self.bind('<Alt-Key-F4>',self.button_testeee)
        
        self.textbox = customtkinter.CTkTextbox(master=self, width=300, corner_radius=0,text_color="green")
        self.textbox.grid(row=5, column=0,padx=(20,10), sticky="nsew")
        
        self.textbox2 = customtkinter.CTkTextbox(master=self, width=200, corner_radius=0,text_color="green")
        self.textbox2.grid(row=5, column=1,padx=(20,0) ,sticky="nsew")
        
        
        
        # definir o controlador
        self.controller:coreController.Controller = None

    def set_controller(self, controller):
        self.controller = controller
        
        
    def button_teste(self):
        self.comunica_arduino.open_connection()
        if self.controller:
            self.controller.teste()
        
    def button_env(self):
        
        file = open('config/teste.txt', 'r', encoding="UTF-8")  # Manipulação de arquivo
        txts = file.readlines()
        file.close()
        
        # Criar uma thread para processar as linhas
        thread = threading.Thread(target=self.processar_linhas, args=(txts,))
        thread.start()
        
    def button_rec(self):
        self.comunica_arduino.read_data()
        
    def button_fechar(self):
        self.comunica_arduino.close_connection()
        
    def button_testeee(self,event):
        self.focus_set()
        print("TESTE")
        
        
    def processar_linhas(self, txts):
        for idx, t in enumerate(txts):
            position = f"{idx + 1}.0"
            self.comunica_arduino.send_data(t)
            self.textbox.insert(position, t)
            self.textbox2.insert("0.0",self.comunica_arduino.read_data())
            time.sleep(5)
        
        
        
        