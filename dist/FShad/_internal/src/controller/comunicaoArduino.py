import serial
import time

class ComunicacaoArduino:
    texto = ""
    
    def __init__(self, port, baud_rate=9600, timeout=1):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial_connection = None

    def open_connection(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            print(f"Conexão com {self.port} estabelecida.")
        except serial.SerialException as e:
            print(f"Erro ao abrir a conexão com {self.port}: {e}")

    def close_connection(self):
        if self.serial_connection:
            self.serial_connection.close()
            print(f"Conexão com {self.port} fechada.")

    def send_data(self, data):
        if self.serial_connection:
            try:
                self.serial_connection.write(data.encode())
                print(f"Dados enviados para {self.port}: {data}")
            except serial.SerialException as e:
                print(f"Erro ao enviar dados para {self.port}: {e}")
        else:
            print("Conexão não aberta. Não é possível enviar dados.")
            

    def read_data(self, num_bytes=12548712):
        if self.serial_connection:
            try:
                data = self.serial_connection.read(num_bytes).decode()
                self.texto = f"Dados recebidos de {self.port}: {data}"
                print(f"Dados recebidos de {self.port}: {data}")
                return data
            except serial.SerialException as e:
                print(f"Erro ao receber dados de {self.port}: {e}")
                return "error"
        else:
            print("Conexão não aberta. Não é possível receber dados.")
            return "Conexão não aberta. Não é possível receber dados."