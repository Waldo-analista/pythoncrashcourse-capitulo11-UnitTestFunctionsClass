from survey import AnonymousSurvey

question='¿Qué lenguaje de programación aprendiste primero?'
encuesta=AnonymousSurvey(question)

encuesta.show_question()

print('Ingresa q para salir en cualquier momento')
while True:
    respuesta=input('Lenguaje:')
    if respuesta=='q':
        break
    else:
        encuesta.store_response(respuesta)

print('Los resultados de la encuesta son: \n')
encuesta.show_results()