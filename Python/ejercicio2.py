#Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

sentence = "Ayer vi a Rosa y me dijo hola y luego se marcho"

query = sentence.find('hola')

print(query)


sentence = "Ayer vi a Rosa y me dijo hola y luego se marcho"
sentence = sentence.replace('hola', 'adios')


print(sentence)


