#calculater 
while True:
    num1 =float(input("Chose a number: "))
    method =(input("Chose the method(+,-,*,/): "))
    num2 =float(input("Chose an anthor number: "))
    

    if method == "+":
        print(num1+num2)
    elif method == "-":
        print(num1-num2)
    elif method == "*":
        print(num1*num2)
    elif method == "/":
        if num2 == 0 :
            print("Error")
        else :
         print(num1/num2)
    else : 
        print("Error")
    

    agian =(input("repeat?(yes/no): "))
    if agian == "yes":
        continue
    if agian == "no":
        print("Proggram ends")
    break 
 

 