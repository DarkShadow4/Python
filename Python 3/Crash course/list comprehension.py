# Without list comprehension
squares1 = []
for value in range(1, 11):
    squares1.append(value**2)
print(squares1)

# With list comprehension
squares2 = [value**2 for value in range(1, 11)]
print(squares2)
