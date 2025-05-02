def determinar_estado_aprobacion(calificaciones):
     while True:
          try:
               calificacion = float(input(f"\033[46mIngresa una calificación de la lista:\033[0m\n{calificaciones}\n>  "))
               
               if calificacion not in calificaciones:
                    raise ValueError("La calificación no está en la lista.")
               
               if 0 <= calificacion <= 100:
                    if calificacion >= 70:
                         print("\033[32mel estudiante ha aprobado\033[0m")
                         break
                    else:
                         print("\033[31mel estudiante ha reprobado\033[0m")
                         break
               else:
                    print("la calificacion debe estar entre 0 y 100")
                    continue
          except ValueError:
               print("\n\033[35mValor invalido. Intenta nuevamente\033[0m\n")

def calcular_promedio(calificaciones):
     suma = sum(calificaciones)
     promedio = suma / len(calificaciones)
     return promedio
def contar_calificaciones_mayores(calificaciones, valor_especifico):
     conteo = sum(1 for x in calificaciones if x > valor_especifico)
     return conteo 
def verificar_calificacion_especifica(calificaciones,calificacion_especifica):
     conteo = 0
     for x in calificaciones:
          if x == calificacion_especifica:
               conteo += 1
     
     return conteo
def main():
     calificaciones = []
     while True:
          try:
               calificaciones = [float (x) for x in input("\033[46mingrese las calificaciones a consultar separadas por comas (ejm. 50,70,80): \033[0m\n>").split(",")]
               break
          except ValueError:
               print("ingrese calificaciones validas")
     while True:
          print("\n\033[46mopciones:\033[0m\n")
          print("\033[36m1.\033[0m Determinar estado de aprobacion")
          print("\033[36m2.\033[0m Calcular promedio")
          print("\033[36m3.\033[0m Contar calificaciones mayores")
          print("\033[36m4.\033[0m Verificar y contar calificaciones especificas")
          print("\033[36m5.\033[0m Salir\n")
          opcion = input("\033[46mingrese una opcion: \033[0m\n> ")
          if opcion == "1":
               determinar_estado_aprobacion(calificaciones)
          elif opcion == "2":
               promedio = calcular_promedio(calificaciones)
               color = "\033[32m" if promedio > 70 else "\033[31m"
               print(f"{color}el promedio de las calificaciones es: {promedio:.2f}\033[0m")
          elif opcion == "3":
               try: 
                    valor_especifico = float(input("\033[46mingrese un valor especifico para comparar: \033[0m"))
                    conteo = contar_calificaciones_mayores(calificaciones,valor_especifico)
                    print(f"\033[32mHay {conteo} calificaciones mayores que {valor_especifico}\033[0m")
               except ValueError: 
                    print(f"ingrese un valor especifico valido")
          elif opcion == "4": 
               try: 
                    calificacion_especifica = float(input("\033[46mingrese una calificacion especifica para validar: \033[0m\n>"))
                    conteo = verificar_calificacion_especifica(calificaciones, calificacion_especifica)
                    if conteo > 0:
                         print(f"\033[34mla calificacion {calificacion_especifica} aparece {conteo} veces\033[0m")
                    else:
                         print(f"\033[35mla calificacion {calificacion_especifica} no aparece en la lista\033[0m")
               except ValueError: 
                    print("ingrese una calificacion especifica valida")
          elif opcion == "5": 
               break 
          else: 
               print("\033[35mopcion invalida. Intente nuevamente\033[0m")

main()