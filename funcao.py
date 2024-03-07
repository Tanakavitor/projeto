def cria_pacote3(arquivo):
    payload = []
    num_tot_pacotes = (len(arquivo) + 49) // 50  # Calcula o número total de pacotes
    for i in range(num_tot_pacotes):
        payload.append(arquivo[i*50:(i+1)*50])  # Divide o arquivo em pacotes de 50 bytes

    head = [b'\x03']  # Cabeçalho inicial
    head.append(num_tot_pacotes.to_bytes(1, byteorder='little'))  # Número total de pacotes
    head.extend([b'\x00'] * 8)  # Preenche o restante do cabeçalho com 0

    eop = b'\xAA\xBB\xCC\xDD'  # Marcador de final de pacote

    pacotes = []
    x = 1
    for i, data in enumerate(payload):
        head[2] = x.to_bytes(1, byteorder='little')  # Número do pacote
        pacote = b''.join(head + [data] + [eop])  # Cria o pacote combinando cabeçalho, dados e marcador de final
        pacotes.append(pacote)
        x+=1
     
    print("numero de pacotes: ", len(pacotes))

    return pacotes

def cria_pacote1(lenpacotes):
    head = [b'\x01']  # Cabeçalho inicial
    #had 1 se refere ao ever
    head.append(b'\x08')  # Identificador do server
    head.append(lenpacotes.to_bytes(1, byteorder='little'))  # Número total de pacotes
    head.extend([b'\x00'] * 7)  # Preenche o restante do cabeçalho com 0
    eop = b'\xAA\xBB\xCC\xDD'  # Marcador de final de pacote
    pacote = b''.join(head + [eop])  # Cria o pacote combinando cabeçalho, dados e marcador de final
    return pacote


def cria_pacote2():
    head = [b'\x02']  # Cabeçalho inicial
    head.append(b'\x08')  # Identificador do server
    head.extend([b'\x00'] * 8)  # Preenche o restante do cabeçalho com 0
    eop = b'\xAA\xBB\xCC\xDD'  # Marcador de final de pacote
    pacote = b''.join(head + [eop])  # Cria o pacote combinando cabeçalho, dados e marcador de final
    return pacote

def cria_pacote4(numpacote):
    head = [b'\x04']  # Cabeçalho inicial
    head.append(b'\x08')  # Identificador do server
    head.append(numpacote.to_bytes(1, byteorder='little'))  # Número do pacote
    head.extend([b'\x00'] * 7)  # Preenche o restante do cabeçalho com 0
    eop = b'\xAA\xBB\xCC\xDD'  # Marcador de final de pacote
    pacote = b''.join(head + [eop])  # Cria o pacote combinando cabeçalho, dados e marcador de final
    return pacote

def cria_pacote5():
    #timeout 
    head = [b'\x05']  # Cabeçalho inicial
    head.append(b'\x08')  # Identificador do server
    head.extend([b'\x00'] * 8)  # Preenche o restante do cabeçalho com 0
    eop = b'\xAA\xBB\xCC\xDD'  # Marcador de final de pacote
    pacote = b''.join(head + [eop])  # Cria o pacote combinando cabeçalho, dados e marcador de final
    return pacote
def cria_pacote6(numero_pacote):
    #mensagem de erro numero correto do paocte enviado na posicao h6
    head = [b'\x06']  # Cabeçalho inicial
    head.append(b'\x08')  # Identificador do server
    head.extend([b'\x00'] * 5)  # Preenche o restante do cabeçalho com 0
    head.append(numero_pacote.to_bytes(1, byteorder='little'))  # Número do pacote
    head.extend([b'\x00'] * 2)  # Preenche o restante do cabeçalho com 0
    eop = b'\xAA\xBB\xCC\xDD'  # Marcador de final de pacote
    pacote = b''.join(head + [eop])  # Cria o pacote combinando cabeçalho, dados e marcador de final
    return pacote





"""
arquivo = b'\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef'
pacotes = cria_pacote3(arquivo)
print("---------------------")
for i in pacotes:
    print(i)  # Imprime cada pacote
    print('')
print("---------------------")
#printa numero de pacotes
print("numero de pacoetes:")
print(len(pacotes))"""