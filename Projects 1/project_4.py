first_number = int(input("enter the first number : "))
second_number = int(input("enter the secound number : "))


for i in range (first_number+1):
    if ( i % second_number == 0):
        print (i)
