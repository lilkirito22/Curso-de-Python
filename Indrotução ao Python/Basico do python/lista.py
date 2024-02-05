# Create an empty list
my_list = []

# Add elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Access elements in the list
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2
print(my_list[2])  # Output: 3

#mostra o indice do elemento
print(my_list.index(2)) # Output: 1

#metodo insert adiciona um elemento em uma posição especifica
my_list.insert(1,4)
print(my_list) # Output: [1, 4, 2, 3]

# last element  in the list
print(my_list[-1])  # Output: 3

#metodo pop remove o elemento de uma posição especifica
my_list.pop(1)
print(my_list) # Output: [1, 2, 3]

#metodo count conta quantas vezes um elemento aparece na lista
my_list.append(1)
print(my_list.count(1)) # Output: 2

# Update an element in the list
my_list[1] = 4
print(my_list)  # Output: [1, 4, 3]

# Remove an element from the list
my_list.remove(3)
print(my_list)  # Output: [1, 4]

# Get the length of the list
print(len(my_list))  # Output: 2


