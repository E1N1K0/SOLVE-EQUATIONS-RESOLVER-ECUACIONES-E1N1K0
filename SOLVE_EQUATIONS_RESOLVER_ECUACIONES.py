'''
Created dec 30, 2021
last updated jan 02, 2022
@author: E1N1K0 

'''
def resolver_ecuacion():                            
    ecuacion_ingresada = str(input('ingresa la ecuacion a evaluar: '))                              # Solicita ingresar una ecuacion.
    ecuacion_espacio = ''.join([i  if i.isalnum() == True
                                   else '' if i == ' ' or i == '_' 
                                   else ' ' + i + ' ' for i in ecuacion_ingresada])                 # Agrega espacios requeridos para separar terminos y simbolos.
    ecuacion_elevado = ecuacion_espacio.replace('*  *','**')                                        # Resuelve el problema de separar los **.
    asignacion = []                                                                                 # Prepara la lista vacia.
    variables = [i for i in set(ecuacion_elevado.split()) if i.isalpha() == True]                   # Separa el string (tipo palabra) y deja solo las variables unicas (con set).
    valores = [asignacion.append(float(input('ingresa ' + i + ': '))) for i in variables]           # Solicita asignar valores de las variables.
    diccionario = {variables[i]:asignacion[i] for i in range(len(variables))}                       # Almacena los valores asignados en un diccionario (solo los valores).
    solucion = [diccionario[i] if i.isalpha() == True 
                               else i for i in ecuacion_elevado.split()]                            # Almacena los valores asignados en diccionario (incorpora simbolos).   
    resultado = ' '.join(map(str,solucion))                                                         # Convierte a string!
    return eval(resultado), print(eval(resultado)), input('presiona cualquier letra para salir')                                                                         # Calcula el string!

# EJECUCION:
resolver_ecuacion()

# y = a + b * x     => escribe solo a + b * x; asigna 1,2,3 resultado = 7
# Area_triangulo, At = base * altura / 2; asigna 2, 4 => resultado = 4
# ecuacion cubica, y = A + B * x + C * x ** 2 + D * x ** 3, asigna 1,2,3,4,5,6 => resultado = 54
# exponente = y = 2 ** x, asigna 2, resultado = 4

# Debería poder superar este ejemplo:
# largo_linea (MM1) = (ritmo_llegadas**2)/(ritmo_servicio*(ritmo_servicio-ritmo_llegadas)); asigna: ritmo_llegadas = 15 persona/h, ritmo_servicio = 20 persona/h => resultado
