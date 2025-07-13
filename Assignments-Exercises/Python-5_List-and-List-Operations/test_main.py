numbers = [5, 3, 8, 1]
print("Original list:", numbers)

# add
numbers.append(6)
print("List after adding an element:", numbers)

# remove
if 8 in numbers:
    numbers.remove(8)
    print("List after removing an element:", numbers)
else:
    print("Element to remove not found in list.")

#sort print
numbers.sort()
print("List after sorting:", numbers)
