numbers = [2, 3, 5, 9, 10]

# add the number at the end of list
numbers.append(12)

# add the number at certain index
numbers.insert(2, 14)

# remove the number
numbers.remove(2)

# clear all data of list
# numbers.clear()

# remove the last item in list
numbers.pop()

# returns the index of item
print(numbers.index(9))

# check the existence of item in list
print(9 in numbers)

# counts number of items that are same
print(numbers.count(14))

# sorts the list assending order
numbers.sort()

# fro decending order add this line
numbers.reverse()

# copy of item
numbers2 = numbers.copy()

print(numbers2)
