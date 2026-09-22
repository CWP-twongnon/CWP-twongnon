my_array = [2, 8, 9, 48, 8, 22, -12, 2]

print(my_array)

result = []

for number in my_array:
    if number > 5:
        result.append(number + 2)

print(set(result))