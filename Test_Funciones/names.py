from name_function import get_formatted_name

print('Ingresa q para salir en cualquier momento')
while True:
    first=input('Ingresa el primer nombre: ')
    if first=='q':
        break
    last=input('Ingresa el apellido: ')
    if last=='q':
        break
    full_name=get_formatted_name(first,last)
    print(f'El nombre completo formateado es: {full_name}')