from src.controller import comunicaoArduino

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
        print(self.view.main_frame.frameNovo_test.textbox.insert("0.0",self.arduino.read_data()))
        
    def fechar_conexao(self):
        self.arduino.close_connection()
        
        
        

    # def save(self, email):
    #     try:
    #         self.model.email = email
    #         self.model.save()
    #         self.view.show_success(f'O email {email} foi salvo!')
        
    #     except ValueError as error:
    #         self.view.show_error(error)