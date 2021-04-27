import random
#A={0,1,2,3,4,5}
#counter ={0:0,1:0,2:0,3:0,4:0,5:0}
#for num in range(100):
count = 0
A_current = 3
while A_current != 0 and A_current != 5:
    randomcoin =random.randint(0,1)*2-1
    A_current = A_current +randomcoin  
    count = count + 1  
    print(A_current)   
print(count)      