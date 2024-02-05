# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

# Access values using keys
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 30
print(my_dict['city'])  # Output: New York

# Update the value of a key
my_dict['age'] = 35

# Remove a key-value pair from the dictionary
del my_dict['city']

# Check if a key exists in the dictionary
if 'name' in my_dict:
  print('Name:', my_dict['name'])

# Iterate over the keys and values in the dictionary
for key, value in my_dict.items():
  print(key, ':', value)