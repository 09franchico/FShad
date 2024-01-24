import customtkinter
from src.controller import coreController

class ConfigViewFrame(customtkinter.CTkFrame):
    def __init__(self, 
                 master,
               **kwargs):
        super().__init__(master, **kwargs)
         
        self.textbox = customtkinter.CTkTextbox(master=self, width=100, corner_radius=0,text_color="green")
        self.textbox.grid(row=0, column=0, sticky="nsew")
        
        self.entry = customtkinter.CTkEntry(self,placeholder_text="inserir texto")
        self.entry.grid(row=1, column=0, padx=(30,10), pady=(15, 5))
        
        self.buttonFechar = customtkinter.CTkButton(self,text="Conectar",command=self.conectar)
        self.buttonFechar.grid(row=2, column=0, padx=(30,10), pady=(15, 5))
        
        self.buttonFechar = customtkinter.CTkButton(self,text="Teste",command=self.button_teste)
        self.buttonFechar.grid(row=3, column=0, padx=(30,10), pady=(15, 5))
        
        self.buttonFecharConexao = customtkinter.CTkButton(self,text="Fechar conexao",command=self.button_fechar)
        self.buttonFecharConexao.grid(row=4, column=0, padx=(30,10), pady=(15, 5))
        
        
        # definir o controlador
        self.controller:coreController.Controller = None

    def set_controller(self, controller):
        self.controller = controller
    
    
    def button_teste(self):
        if self.controller:
            self.controller.config_env()
            #self.controller.enviar_dado_arduino(self.entry.get())
        
    
    def conectar(self):
        if self.controller:
            self.controller.conexao_arduino()
            
    def button_fechar(self):
        if self.controller:
              self.controller.fechar_conexao()
              
    
        