# Python Program to Put Even and Odd Numbers in Separate List

numbers = []
even_numbers = []
odd_numbers = []

Number = int(input("How many elements in list : "))

for i in range(1, Number + 1):
    value = int(input(f"Please enter the Value of {i} Element : " ))
    numbers.append(value)

for j in range(Number):
    if(numbers[j] % 2 == 0):
       even_numbers.append(numbers[j])
    else:
        odd_numbers.append(numbers[j])

print(f"\n  Even numbers is : {even_numbers} ")
print(f"\n  Odd numbers is : {odd_numbers}")
