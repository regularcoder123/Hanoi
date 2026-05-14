r1 = [1,2,3]
r2 = []
r3 = []
playing = True
def display(r1,r2,r3):
    print("1 is small, 2 is medium, 3 is big.")
    print(f"Rod 1 -->{r1}")
    print(f"Rod 2 -->{r2}")
    print(f"Rod 3 --> {r3}")
def gamerules(r1,r2,r3):
    if r1[0] == 2  and r1[1] == 1:
        print("Invalid move")

while True:
    gamerules(r1,r2,r3)
    display(r1,r2,r3)
    ring_name = int(input("Enter the ring number:"))
    rod_origin = int(input("Which rod to start?: r1 - 1, r2-2, r3-3:"))
    rod_destination = int(input("Which rod do you want to move this ring too? r1 - 1, r2-2, r3-3:"))

    # ring 1
    if ring_name == 1:
        if rod_origin == 1:
            r1.remove(ring_name)
            if rod_destination == 2:
                r2.append(ring_name)
                r2.reverse()
                display(r1,r2,r3)
            if rod_destination == 3:
                r3.append(ring_name) 
                r3.reverse()  
                display(r1,r2,r3)        
        if rod_origin == 2:
            r2.remove(ring_name)
            if rod_destination == 1:
                r1.append(ring_name)
                r1.reverse()
                display(r1,r2,r3)
            if rod_destination == 3:
                r3.append(ring_name)
                r3.reverse()   
                display(r1,r2,r3)   
        if rod_origin == 3:
            r3.remove(ring_name)
            if rod_destination == 2:
                r2.append(ring_name)
                r2.reverse()
                display(r1,r2,r3)
            if rod_destination == 1:
                r1.append(ring_name)
                r1.reverse()   
                display(r1,r2,r3)
    #ring 2

    if ring_name == 2:
        if rod_origin == 1:
            r1.remove(ring_name)
            if rod_destination == 2:
                r2.append(ring_name)
                r2.reverse()
                display(r1,r2,r3)
            if rod_destination == 3:
                r3.append(ring_name)  
                r3.reverse() 
                display(r1,r2,r3)        
        if rod_origin == 2:
            r2.remove(ring_name)
            if rod_destination == 1:
                r1.append(ring_name)
                r1.reverse()
                display(r1,r2,r3)
            if rod_destination == 3:
                r3.append(ring_name)
                r3.reverse()   
                display(r1,r2,r3)   
        if rod_origin == 3:
            r3.remove(ring_name)
            if rod_destination == 2:
                r2.append(ring_name)
                r2.reverse()
                display(r1,r2,r3)
            if rod_destination == 1:
                r1.append(ring_name) 
                r1.reverse()  
                display(r1,r2,r3) 
    #ring 3

    if ring_name == 3:
        if rod_origin == 1:
            r1.remove(ring_name)
            if rod_destination == 2:
                r2.append(ring_name)
                r2.reverse()
                display(r1,r2,r3)
            if rod_destination == 3:
                r3.append(ring_name)  
                r3.reverse() 
                display(r1,r2,r3)        
        if rod_origin == 2:
            r2.remove(ring_name)
            if rod_destination == 1:
                r1.append(ring_name)
                r1.reverse()
                display(r1,r2,r3)
            if rod_destination == 3:
                r3.append(ring_name)
                r3.reverse()   
                display(r1,r2,r3)   
        if rod_origin == 3:
            r3.remove(ring_name)
            if rod_destination == 2:
                r2.append(ring_name)
                r2.reverse()
                display(r1,r2,r3)
            if rod_destination == 1:
                r1.append(ring_name) 
                r1.reverse()  
                display(r1,r2,r3)
    
    

       
        
        
        
        

        

    
