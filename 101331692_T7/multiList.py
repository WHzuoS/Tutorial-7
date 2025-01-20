from random import randint
list = [[],[],[]]

for i in list:
    for j in range(3):
        random_number = randint(1,25)
        i.append(random_number)

product = 1

for k in list:
    for l in range(3):
        product *= k[l]

print(f"This is your multi-dimensional list: {list}")
print(f"This is the product of all elements: {product}")