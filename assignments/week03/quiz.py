# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:



# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")

        if choice == "1":
             print("Balance ", balance ,"Bath")
        elif choice == "2":
             wd = float(input("Amount:"))
        elif choice == "3":
            dp = float(input("Amount"))
        elif choice == "4":
            break
 
else:
    print("Invalid PIN")
