"""
Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y
que los valide utilizando los módulos generados en los dos ejercicios anteriores.
Ayuda: para contar la cantidad de caracteres de una cadena, en Python se utiliza la
función incorporada: len(cadena)
"""
import usuario
import passw

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if usuario.nickname(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if passw.clave(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False