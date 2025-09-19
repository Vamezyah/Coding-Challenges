import random
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','/','=','?','¡','¿','+','*','-','_']

print("Welcome to the password generator")
nn = int(input("How many numbers would you like in your password? \n"))
ns = int(input("How many symbols would you like in your password? \n"))
nl = int(input("How many letters would you like in your password? \n"))

count = nn + ns + nl
password = ''
resta = 0
i = 0
while i < count:
    choice = random.randint(1,3)
    i -= resta
    if (choice == 1):
        if nn == 0:
            resta = 1
        else:
            caracter = random.randint(0,9)
            password = password + numbers[caracter]
            nn -= 1
            resta = 0
    if (choice == 2):
        if ns == 0:
            resta = 1
        else:
            caracter = random.randint(0,13)
            password = password + symbols[caracter]
            ns -= 1
            resta = 0
    if (choice == 3):
        if nl == 0:
            resta = 1
        else:
            caracter = random.randint(0,26)
            letra = letters[caracter]
            if random.randint(0,1) == 1:
                letra = letra.upper()
            password = password + letra
            nl -= 1
            resta = 0
    
    if (len(password) <= count):
        if ((ns == 0 and nl == 0 and nn > 0) or (ns == 0 and nl > 0 and nn == 0) or (ns > 0 and nl == 0 and nn == 0)):
            resta = 1
    
    i += 1

    if (ns == 0 and nl == 0 and nn == 0):
        i = count

print(password)
