import os 
os.system('cls')
titulo="""
***************
NUMEROS PRIMOS 
***************
"""
Catalogo_de_operaciones ="1. primo o compuesto \n2.  verificar cuantos de los numeros ingresados son primos \n3. lista de primos menores que \n4.  el numero de primos menores que \n5. factores primos\n6. numero par como entrada\n7 preguntas\n8.  salir"
isactive=True
while True:
     print(titulo)
     print(Catalogo_de_operaciones)

     op = int(input("por favor selecciona una opción) "))
     # Pedir función 
     if op ==1:
          def num_primo(n):
               if n < 2:#los números primos son enteros positivos mayores que 1.
                    return False
               for i in range (2, n):
                    if n % i == 0: 
                         return False
               return True
          n=int(input("ingresa un numero para comprobar si es primo o compuesto "))
          if num_primo(n):
               print(f"{n} es numero primo")
          else:
               print(f"{n} no es numero primo")
          os.system('pause')
     if op ==2:
          cantidad_primos=0
          n=0
          nums=[]
          def num_primo(n):
               if n < 2:#los números primos son enteros positivos mayores que 1.
                    return False
               for i in range (2, n):
                    if n % i == 0: 
                         return False
               return True
          def contar(n):# contara los numeros que el usuario ingrese que sean mayores a 0
               contar = 0
               for num in n:
                    if num_primo(num):
                         contar +=1 #si el numero es primo lo sumará o contará
               return contar
          while True:
               cantidad_primos=int(input("por favor, ingresa la cantidad de numeros que desea contar "))
               if cantidad_primos >= 0:
                    break #si el usuario ingresa el numero 0 el programa se rompe ya que se cuentan positivos mayores que 1.
               else:
                print("ingresa un numero mayor a '0', por favor")
          for i in range (1, cantidad_primos + 1):
                    n=int(input(f"Ingresa el numero {i}: "))
                    nums.append(n)
          num_primos =contar(nums)
          print(f"De los numeros que ingresaste,{num_primos} son primos ")
          os.system('pause')
     if op ==3:
          m=0
          numero=0
          num_ingresado=2
          primos=[]
          def num_primo(n):
               if n < 2:#los números primos son enteros positivos mayores que 1.
                    return False
               for i in range (2, n):
                    if n % i == 0: 
                         return False
               return True
          
          def numprimos_menores(m):
               for numero in range (2,m):#se buscan numeros desde el 2 en adelante
                    if num_primo(numero):
                        primos.append(numero)
               return primos
          
          m=int(input("Ingresa un numero para hallar los primos menores "))
          if m < 2:
               print("por favor ingresa un numero mayor a '2' para ejecutar el programa ")
          else:
               respuesta=numprimos_menores(m)
               print(f"Los numeros primos menores que {m} son: {primos} ")
          os.system('pause')
     if op ==4:
           l=0
           n=0
           contar=0
           contar_primos=0

           def num_primo(n):
               if n < 2:#los números primos son enteros positivos mayores que 1.
                    return False
               for i in range (2, n):
                    if n % i == 0: 
                         return False
               return True
           def numero_primos_menores(l):
               contar = 0
               for number in range(2, l):
                    if num_primo(number):
                         contar += 1
               return contar
           l= int(input("por favor, ingresa un numero para contar los primos menores: "))

           if l < 2:
                print("Por favor, ingresa un numero mayor a '2' para ejecutar el programa.")
           else:
                contar_primos= numero_primos_menores(l)
                print(f"el numero de primos menores que {l} es: {contar_primos}")
           os.system('pause')
     if op==5:
          def factor_par(a):
               factor = []
               divisor = 2
               while (divisor * divisor <= a):
                    if a % divisor:
                         divisor += 1
                    else:
                         a //= divisor
                         factor.append(divisor)
               if a > 1:
                    factor.append(a)
               return factor
          num = int(input("Ingresa un número entero para mostrar sus factores primos: "))
          if num < 2:
               print("Por favor, ingresa un número entero mayor o igual a '2'.")
          else:
               lista_factores = factor_par(num)
               print(f"Los factores primos de {num} son: {lista_factores}")
          os.system('pause')
     if op==6:
          import os
          def ingresar_par(numero):
               if numero < 2:
                    return False
               for i in range(2, int(numero ** 0.5) + 1):
                    if numero % i == 0:
                         return False
               return True

          def obtener_primos(num):
               return [i for i in range(2, num) if ingresar_par(i)]

          def mostrar_sumas_de_primos(num_par):
               if not (num_par % 2 == 0 and num_par >= 4):
                    print("Por favor, ingresa un número par mayor o igual a 4.")
                    return

               primos = obtener_primos(num_par)
               par_dict = {primo: True for primo in primos}

               for primo in primos:
                    complemento = num_par - primo
                    if complemento in par_dict and primo <= complemento:
                         print(f"{primo} + {complemento}")

               # Solicitar entrada del usuario después de definir las funciones
               num_par = int(input("Ingrese un número par mayor o igual a 4: "))
               mostrar_sumas_de_primos(num_par)
               os.system('pause')



               

     
     

