from src.controller import comunicaoArduino
import time
import threading

class Controller:
    
    def __init__(self, arduino:comunicaoArduino.ComunicacaoArduino, views):
        self.arduino = arduino
        self.view = views
        
    def teste(self):
        print("OLa mundo que legal essa parada aqui")
        
    def conexao_arduino(self):
        self.arduino.open_connection()
    
    def enviar_dado_arduino(self,data):
        self.arduino.send_data(data)
        # print(self.view.main_frame.frameNovo_test.textbox.insert("0.0",self.arduino.read_data()))
        
    def fechar_conexao(self):
        self.arduino.close_connection()
        
    def config_env(self):
        
        file = open('config/teste.txt', 'r', encoding="UTF-8")  # Manipulação de arquivo
        txts = file.readlines()
        file.close()
        
        # Criar uma thread para processar as linhas
        thread = threading.Thread(target=self.processar_linhas, args=(txts,))
        thread.start()
        
        
    def processar_linhas(self, txts):
        for idx, t in enumerate(txts):
            position = f"{idx + 1}.0"
            self.arduino.send_data(t)
            self.view.main_frame.frameNovo_test.textbox.insert(position,t)
            time.sleep(5)
        
        
        

    # def save(self, email):
    #     try:
    #         self.model.email = email
    #         self.model.save()
    #         self.view.show_success(f'O email {email} foi salvo!')
        
    #     except ValueError as error:
    #         self.view.show_error(error)