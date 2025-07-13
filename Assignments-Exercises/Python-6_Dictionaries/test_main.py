# create dictionary
dictionary = {'name': 'Sparky', 'age': 25}
print("Original dictionary:", dictionary)

# Step 2: Add a new key-value pair
dictionary['city'] = 'New York'
print("Dictionary after adding an item:", dictionary)

# Step 3: Update an existing key-value pair
dictionary['age'] = 26
print("Dictionary after updating an item:", dictionary)

# Step 4: Remove a key-value pair
removed_value = dictionary.pop('age')
print("Dictionary after removing an item:", dictionary)
