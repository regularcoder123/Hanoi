user_number = int(input("Please choose a number to test:"))
factors = []
if user_number != 1:
    for i in range(2,user_number - 1):
        remainder = user_number % i
        if remainder == 0:
            factors.append(i)
        else:
            pass
    if factors == []:
        print(f"{user_number} is a prime number")
        
    else:
        print(f"{user_number} is composite")
        
      
else:
    print("1 is a unique number, please choose another number.")
    
