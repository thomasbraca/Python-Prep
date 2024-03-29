class Funcionesnuevas:
    def __init__(self,lista_numeros):
       self.lista=lista_numeros

    def es_primo(self):
        for i in self.lista:
            if self.__es_primo(1):
                print('El numero', i, 'es primo')
            else:
                print('El numero', i, 'no es primo')

    def conversion_grados(self,origen,destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i,origen,destino), 'grados', destino) 

    def factorial(self):
        for i in self.lista:
            print('El factorial de',i,'es',self.__factorial(i))

    def __es_primo (self,numero):
        primo=True
        for i in range(2,numero):
            if numero%i==0:
                primo=False
                break
        return primo
    def mas_repetido(self):
        lista_valor=[]
        lista_repeticiones=[]
        if len(self.lista)==0:
            return None
        for elemento in self.lista:
            if elemento in lista_valor:
                i = lista_valor.index(elemento)
                lista_repeticiones[i]+=1
            else:
                lista_valor.append(elemento)
                lista_repeticiones.append(1)
        valor_mas_repetido = lista_valor[0]
        cantidad_de_repeticiones = lista_repeticiones[0]

        for i,elemento in enumerate(lista_repeticiones):
            if lista_repeticiones[i]>cantidad_de_repeticiones:
                valor_mas_repetido=lista_valor[i]
                cantidad_de_repeticiones=lista_repeticiones[i]
        return valor_mas_repetido, cantidad_de_repeticiones
    def __conversion_grados (self,valor, origen, destino):
        if origen=="celsius":
            if destino=="celsius":
                return valor
            
            elif destino=="farenheit":
                return (valor*9/5)+32
            
            elif destino=="kelvin":
                return valor + 273.15
            else:
                print("Parametro de destino incorrecto")
        elif origen=="farenheit":
            if destino=="celsius":
                return (valor-32)*5/9
            
            elif destino=="farenheit":
                return valor
            
            elif destino=="kelvin":
                return ((valor-32)*5/9) + 273.15
            else:
                print("Parametro de destino incorrecto")
        elif origen=="kelvin":
            if destino=="celsius":
                return valor - 273.15
            
            elif destino=="farenheit":
                return ((valor - 273.15)*9/5)+32
            
            elif destino=="kelvin":
                return valor 
            else:
                print("Parametro de destino incorrecto")
        else:
            print("Parametro de origen incorrecto")

    def __factorial (self,numero):
        if type(numero)!= int:
            return "El numero debe ser un entero"
        if numero<0:
            return "El numero debe ser positivo"
        if numero <= 1:
            return 1
        
        numero = numero*self.__factorial(numero-1)
        return numero