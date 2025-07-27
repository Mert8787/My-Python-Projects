#Project: Temp Converter
# This program converts temperature from Celsius to Fahrenheit
# Author: Mert
while True:
    print("----------------------------------------")
    print(" Welcome to the Temperature Converter!")
    print("----------------------------------------")
    c = (input('Enter temperature in Celsius: ')) 

    f =  (9/5) * int(c) + 32 

    print(f"\nThe temperature in Fahrenheit is {f} Degree")

    print("----------------------------------------")

    agian =(input("Repeat?(yes/no): "))
    if agian == "yes":
        print("\nThe temperature converter is running again...\n")
        continue
    if agian == "no":
        print("----------------------------------------")
        print("\nTemperature convecter ends\n")
        print("----------------------------------------")
    break 
    
