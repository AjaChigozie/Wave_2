# Use this playground to experiment with list methods, using Test Run

# List Methods
character_names = ['Rowan Row', 'Jeremy Irons', 'Anna Delaney', 'Felicity Smoak', 'Chloe Sullivan', 'Barbra Gordon']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Len() method
print(len(character_names))
print(len(numbers), '\n')

# Max() Method
print(max(character_names))
print(max(numbers), '\n')

# Min() Method
print(min(character_names))
print(min(numbers), '\n')

# reverse() method
character_names.reverse()
print(character_names)
numbers.reverse()
print(numbers, '\n')

# pop () method
character_names.pop(4)
print(character_names)
numbers.pop(5)
print(numbers, '\n')

# Append() Method
character_names.append('Jared Leto')
print(character_names)
numbers.append(10)
print(numbers, '\n')

# Sort() method
character_names.sort()
print(character_names)
numbers.sort(reverse=True)
print(numbers, '\n')

# sorted() method
sort = sorted(numbers), sorted(character_names, reverse=True)
print(sort, '\n')

# remove() method
character_names.remove(character_names[3])
print(character_names)
numbers.remove(10)
print(numbers, '\n')

# count() method
name = character_names.count("Jared Leto")
print(name, '\n')

# clear() method
numbers.clear()
print(numbers)

