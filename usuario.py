"""
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:
• El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
• El nombre de usuario debe ser alfanumérico
• Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de
usuario debe contener al menos 6 caracteres”
• Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de
usuario no puede contener más de 12 caracteres”
• Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje
“El nombre de usuario puede contener solo letras y números”
• Nombre de usuario válido, retorna True
"""

def nickname(nombre_usuario):

        long=len(nombre_usuario) #Calcular la longitud del nomre de usuario
        y=nombre_usuario.isalnum() #Calcula que la cadena contenga valores alfanuméricos
        
        if y== False: # La cadena contiene valores no alfanuméricos
            print("El nombre de usuario puede contener solo letras y números")
            
        if long < 6: 
            print("El nombre de usuario debe contener al menos 6 caracteres")
            
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            return True #Verdadero si el tamaño es mayor a 5 y menor a 13

            
print(nickname("sergiocamilocastillo"))