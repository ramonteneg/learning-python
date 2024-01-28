num
1
2
3

Contador => c = c + K => K es una constante
Incremento consecutivo y constante.
cont = cont + 1 //cont++ //cont+=1

Acumulador => a = a + V => V es una variable (num, salario, edad, temperaturas, etc.)
Incremento aleatorio y variable.
acum = acum + num //acum+=num



def list_numbers():
  
    i = 1
    while i <= 100:
        print(i)
        i+=1 #i = i + 1

    print("i:", i) #101

def list_numbers2():
    i = 1
    status = True
    while status: #while status == True
        if i == 11:
            break 
        print(i)
        i+=1 #i = i + 1

    print("i:", i) #101

def list_numbers3():
    i = 1
    status = True
    while status: #while status == True 
        print(i)
        i+=1 #i = i + 1
        if i > 10 : # i == 11
            status = False

    print("i:", i) #11

def list_numbers4():
    i = 1
    status = False
    while not status: #while status != False 
        print(i)
        i+=1 #i = i + 1
        if i > 10 : # i == 11
            status = True

    print("i:", i) #11

#list_numbers()
#ist_numbers2()
#list_numbers3()
list_numbers4()    
