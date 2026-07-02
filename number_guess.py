number=2
user=int(input("enter the number: "))
while user!=number:
    if user < number:
        print("too low")
    elif user> number:
        print("to high")
        
    user=int(input("enter the number again: "))
print("you win🌟")