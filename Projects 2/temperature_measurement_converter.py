#convert Fahrenheit to Celcius and back
user = input("Enter type of convert (Temperature as (T) Measurement as (M):")

def temp_convert():
    select = input("Select type of temperature (Fahrenheit as F , Celsius as C): ")
    if select ==  "C":
        temp = int(input("Enter temperature with Celsius : "))
        culc = ((9 * temp) / 5 + 32)
        print ("The temperature in Celsius",culc)
    elif select == "F":
        temp = int(input("Enter temperature wit Fahrenheit: "))
        culc = ( temp - 32) * 5 / 9
        print ("The temperature in Fahrenheitis",culc)
    else:
        print("Try agine")
#convert inches to centimeters and back
def Measurement_convert():
    select = input("Select type of Measurement ( Inches as I , Centimeters as C): ")
    if select ==  "I":
        mesuer = int(input("Enter Measurement with Inches : "))
        culc = (2.54*mesuer)
        print ("The Measurement in Centimeters",culc)

    elif select == "C":
        mesuer = int(input("Enter Measurement wit Centimeters: "))
        culc = (mesuer/2.54) 
        print ("The Measurement in Inches",culc)
    else:
       print("Try agine")

if user == "T":
    temp_convert()
elif user == "M":
    Measurement_convert()
