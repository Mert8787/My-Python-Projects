#project 2 clients tracker


file_path =" C:\\Users\\yazan\\OneDrive\\Documents\\Desktop\\Clients tracker.txt"

class Client :
   def __init__(self, name , email , date):
        self.Name = name 
        self.email = email 
        self.Date = date
         
   def save_client(self):
    file_path = r"C:\Users\yazan\OneDrive\Documents\Desktop\Clients tracker.txt"
    with open(file_path, "a") as file:
        file.write(f"Name [{Name}] , Email [{Email}] , due date in [{Date}]\n")

def show_clients(filepath):
    print ("\nclients list\n")
   
    file_path = r"C:\Users\yazan\OneDrive\Documents\Desktop\Clients tracker.txt"
    try :
      with open (file_path , "r") as file:
       for line in file:
        print(line.strip())
    except FileNotFoundError :
       print("File doesnt Exits!") 

while True :
    print("Chose an option  : ")
    print("1. Add client")
    print("2. Show all Clients")
    print("3. Exit")

    option=(input("Option: "))

    if  option == "1" :
        print("Add the client info")
        Name = (input("Client name: "))
        Email = (input("Client Email : "))
        Date = (input("The due Date : "))
        

        client = Client(Name, Email, Date)
        client.save_client()
       
        print("\nClient Saved\n")
        
        print("1. Menu")
        print("2. Exit")
        
        choice=(input("Choice : "))
        if choice == "1":
           print()
           continue
        elif choice == "2":
           print()
           print("Thank you , ")
           break
        
    elif option == "2" :
         show_clients(file_path)
        
         print("\n1. Menu")
         print("2. Exit")
        
         choice=(input("\nChoice : "))
         if choice == "1":
           print()
           continue
         elif choice == "2":
           print()
           print("  Thank you , ")
           break
        
    elif option == "3": 
      
       print("\n               Thank you \n")
       break