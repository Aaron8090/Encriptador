from array import array
import getpass

input("Ingresa el usuario: ")
counter = 1
password = getpass.getpass("Ingresa el contraseña: ")
while password != "Dejame entrar":
    counter = counter + 1
    password = getpass.getpass("Contraseña incorrecta, vuelve a intentar: ")
    if counter == 5:
        print("Llegaste al limite de intentos")
        exit()

print("-----------------------------------------------------------")
mensaje = input("Ingresa el mensaje:")
separaMensaje = list(mensaje.lower())
abecedario = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.']
numEncriptar = []
aux = 0

espacio = 0
punto = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
ñ = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0


for i in separaMensaje:
    if(i == 'a'):
        a = 1
        numEncriptar.append(1)
        #print(1)
    
    if(i == 'b'):
        b = 2
        numEncriptar.append(2)
        #print(2)
    
    if(i == 'c'):
        c = 3
        numEncriptar.append(3)
        #print(3)
    
    if(i == 'd'):
        d = 4
        numEncriptar.append(4)
        #print(4)
    
    if(i == 'e'):
        e = 5
        numEncriptar.append(5)
        #print(5)
    
    if(i == 'f'):
        f = 6
        numEncriptar.append(6)
        #print(6)

    if(i == 'g'):
        g = 7
        numEncriptar.append(7)
        #print(7)

    if(i == 'h'):
        h = 8
        numEncriptar.append(8)
        #print(8)

    if(i == 'i'):
        i = 9
        numEncriptar.append(9)
        #print(9)

    if(i == 'j'):
        j = 10
        numEncriptar.append(10)
        #print(10)

    if(i == 'k'):
        k =11
        numEncriptar.append(11)
        #print(11)

    if(i == 'l'):
        l = 12
        numEncriptar.append(12)
        #print(12)

    if(i == 'm'):
        m = 13
        numEncriptar.append(13)
        #print(13)

    if(i == 'n'):
        n = 14
        numEncriptar.append(14)
        #print(14)

    if(i == 'ñ'):
        ñ = 15
        numEncriptar.append(15)
        #print(15)

    if(i == 'o'):
        o = 16
        numEncriptar.append(16)
        #print(16)

    if(i == 'p'):
        p = 17
        numEncriptar.append(17)
        #print(17)

    if(i == 'q'):
        q = 18
        numEncriptar.append(18)
        #print(18)

    if(i == 'r'):
        r = 19
        numEncriptar.append(19)
        #print(19)

    if(i == 's'):
        s = 20
        numEncriptar.append(20)
        #print(20)

    if(i == 't'):
        t = 21
        numEncriptar.append(21)
        #print(21)

    if(i == 'u'):
        u = 22
        numEncriptar.append(22)
        #print(22)

    if(i == 'v'):
        v = 23
        numEncriptar.append(23)
        #print(23)

    if(i == 'w'):
        w = 24
        numEncriptar.append(24)
        #print(24)
        
    if(i == 'x'):
        x = 25
        numEncriptar.append(25)
        #print(25)

    if(i == 'y'):
        y = 26
        numEncriptar.append(26)
        #print(26)

    if(i == 'z'):
        z = 27
        numEncriptar.append(27)
        #print(27)

    if(i == '.'):
        punto = 28
        numEncriptar.append(28)
        #print(28)
        
    if(i == ' '):
        espacio = 0
        numEncriptar.append(0)
        #print(0)

matriz = [[1, 2, 1], [0, -1, 3], [2, 1, 0]]

for aa in range(0, len(numEncriptar)):
    for bb in range(0, 3):
        aux = (matriz[0][bb] * numEncriptar[aa]) + (matriz[1][bb] * numEncriptar[aa + 1]) + (matriz[2][bb] * numEncriptar[aa + 2])
        print(aux, end=' ')
aa+=2
