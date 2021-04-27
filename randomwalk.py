import random
count =0
rw = 1
for num in range(1,1000):
    while rw!= 0 and rw!= -1:
        if rw == 1:    
            rw =random.randint(1,4)
            if rw == 1:
                rw = 2
            elif rw == 2:
                rw = 4
            else:
                rw = 0
        elif rw == 2:
            rw =random.randint(1,4)
            if rw == 1:
                rw = 1
            elif rw == 2:
                rw = 3
            elif rw == 3:
                rw = 5
            else :
                rw =0               
        elif rw == 3:
            rw =random.randint(1,3)
            if rw == 1:
                rw = 2
            elif rw == 2:
                rw = 6
            else:
                rw =0        
        elif rw == 4:
            rw =random.randint(1,4)
            if rw == 1:
                rw = 2
            elif rw == 2:
                rw = 6
            elif rw ==3:
                rw =0
            else:
                rw =-1      
        elif rw == 5:
            rw =random.randint(1,4)
            if rw == 1:
                rw = 4
            elif rw == 2:
                rw = 2
            elif rw == 3:
                rw =6
            else:
                rw =-1
        elif rw ==6:
            rw =random.randint(1,2)
            if rw == 1:
                rw = 3
            else:
                rw =5
    if rw ==-1:
        count += 1  
print(num-count,count)     
