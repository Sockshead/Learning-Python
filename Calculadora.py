while True:
   print("Calculadora")
   print("1. Suma")
   print("2. Resta")
   print("3. Multiplicacion")
   print("4. Division")
   print("5. Salir")
   user_input = input("Ingrese el numero de la opcion que desea utilizar: ")

   if user_input == "5":
      break
   elif user_input == "1":
      a = float(input("Ingrese el primer digito: "))
      b = float(input("Ingrese el segundo digito: "))
      resultado=str(a + b)
   elif user_input == "2":
      a = float(input("Ingrese el primer digito: "))
      b = float(input("Ingrese el segundo digito: "))
      resultado = str(a - b)
   elif user_input == "3":
      a = float(input("Ingrese el primer digito: "))
      b = float(input("Ingrese el segundo digito: "))
      resultado = str(a * b)
   elif user_input == "4":
      a = float(input("Ingrese el primer digito: "))
      b = float(input("Ingrese el segundo digito: "))
      if(b==0):
          resultado = "indefinido"
      else:
         resultado = str(a / b)
   else:
       resultado = "una opcion invalida, por favor digite una de las opciones existentes"
   print("El resultado es " + resultado)
   print("\n")