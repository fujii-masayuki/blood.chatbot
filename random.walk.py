import random
All={0,1,100,200,300,400,500,600}
counter = {0:0,1:0}

current=100
randomcoin = random.randint(0,4)

while current !=0 and current !=1:
    if randomcoin ==1 or  randomcoin ==2:
            current = 0
    elif randomcoin ==3:
            current = 200
    else:
            current = 300
print(current)                 



