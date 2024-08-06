#Formar Número inteiro em número romano
def int_to_rome(num):
    x = int(num)
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
    i = 12  
    roman_numeral = ''
    while x != 0:
        if numbers[i] <= x:    
            roman_numeral += roman[i] 
            x = x - numbers[i]
        else:
            i -= 1 # i = i - 1
    return roman_numeral 


#formar numero romano em real
def lista_romanos(romano):
    roma = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}  
    total = 0
    previo = 0

    for simbolo in reversed(romano):
        valor = roma[simbolo]
        if valor <  previo:
            total -= valor    
                 
        else:
            total += valor
            previo = valor
    return total  




#verificar qual o tipo de conversão se é para decimal ou romano
def DiferenciarNumero(numero):
      while True:
          num = input(numero)
          if not num.isdigit():
             Num = VerificarLetra(num)   

             if Num != None:
              print(Num)   

          else:
             Num =   int_to_rome(num)
             if Num != None:
                 print(Num)


#verificar letra
def VerificarLetra(letra):
    fraseverificacao = letra.upper()    
    if not all(char.isalpha() or char.isspace() for char in fraseverificacao):
         print("\033[0;31mOPS! Valores inválidos.\033[m")
    else:
        romano = fraseverificacao
        Num = lista_romanos(romano)
        return Num
    


if __name__ == "__main__":
    numero = DiferenciarNumero("Digite um Número Romano ou um Número Inteiro:  ")
    