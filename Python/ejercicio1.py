#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

name = "Cecilia"
age = 25
list = ["mesa", "sofa", "almohada" ]
boolean = True

print(name)
print(age)
print(list)
print(boolean)


#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

name = "Cecilia"
third_word = name [:3]

print(third_word)


#Exercise 3: Use an index to grab the first element from your list.

list = ["mesa", "sofa", "almohada"]

print(list[0])

#Exercise 4: Create a new number variable that adds 10 to your original number.

new_number = 250

new_number += 10

print(new_number)


#Exercise 5: Use an index to get the last element in your list.

list = ["mesa", "sofa", "almohada"]

print(list[-1:])


#Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')

print(list_of_names)


#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

string = 'Creacion de variables con mayusculas'

first_word = string.split()[0]

print(first_word)


string = 'Creacion de variables con mayusculas'

print(string.upper())


varstr = 'Creacion de variables con mayusculas'

str_mayus = varstr[:8].upper()


particion1, _, particion2 = varstr.partition(' ')


str_final = str_mayus +' '+ particion2
print(str_final)


#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

name = "Cecilia"
age = 25

greeting = f'Hi I am {name}, I am {age} years old'

print(greeting)



#Exercise 9: Print “hello world”.

greeting = "Hello World"

print(greeting)

