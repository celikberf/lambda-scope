"""
#liste elemanlarının karesini aldık . 

def square(num): 
    return num ** 2

numbers = [1,3,5,9]

map(square,numbers) # tek tek yapmak yerine...

#karesini alıp liste şeklinde yazdık
result = list(map(square,numbers))
print(result)

#karesini alıp yanyana yazdık
for item in map(square,numbers):
    print(item)

"""

"""
#daha kısa yöntemi lambda ile : 


numbers = [1,3,5,9]

result = list(map(lambda num: num ** 2,numbers))

print(result)

# 2. bir yazış
square = lambda num : num ** 2
numbers = [1,3,5,9]

result = list(map(square,numbers))

print(result)

"""


numbers = [1,3,5,9,10,4]

def check_even(num): return num % 2 == 0

result = list(filter(lambda num: num % 2 == 0 , numbers))

print(result)

# ya da

numbers = [1,3,5,9,10,4]

check_even = lambda num : num % 2 == 0

result = list(filter(check_even,numbers))
print(result)