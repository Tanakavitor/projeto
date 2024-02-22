from enlace import *
import time
import numpy as np
import random

serialName = "COM4"  # Defina a porta serial corretamente

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)
        com1.enable()
        print("esperando 1 byte de sacrifício") 
        rxBuffer, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)


        # Gerar os dados a serem transmitidos (txBuffer)
        # txBuffer = b'\x12\x13\xAA'  # Exemplo de dados a serem transmitidos

        # Calcular o tamanho dos dados a serem enviados
        # txLen = len(txBuffer)
        # print("Tamanho dos dados a serem enviados:", txLen)

        # Transmitir os dados
        # print("Iniciando transmissão...")
        # com1.sendData(txBuffer)
        # print("Transmissão concluída!")

        # A recepção de dados acontece automaticamente em um thread separado no enlace

        # Receber os dados
        print("Aguardando recebimento de dados...")
        rxBuffer, nRx = com1.getData(10)  # Defina o tamanho esperado dos dados recebidos
        print("Recebeu {} bytes".format(nRx))

        # Salvar os dados recebidos em um arquivo
        # with open("received_data.bin", "wb") as f:
        #     f.write(rxBuffer)
        # print("Dados recebidos salvos com sucesso!")

        # Exibir os dados recebidos
        print("Dados recebidos:", rxBuffer)

        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()

if __name__ == "__main__":
    main()
