import random
numero = random.randint(10, 30)
comando_1 = 0x00000000
comando2 = 0x0000FF00
comando_3 = 0xFF0000
comando_4 = 0x00FF00
comando_5 = 0x0000FF
comando_6 = 0x00FF
comando_7 = 0xFF00
comando_8 = 0x00
comando_9 = 0xFF
#Coloque tudo em uma lista
comandos = [comando_1,comando2,comando_3,comando_4,comando_5,comando_6,comando_7,comando_8,comando_9]
nova_lista = []
for i in range(numero):
    novo_numero = random.randint(0, 8)
    nova_lista.append(comandos[novo_numero])
    
nova_lista2 = []
for i in range(numero):
    nova_lista2.append(hex(nova_lista[i]))
print(nova_lista2)

