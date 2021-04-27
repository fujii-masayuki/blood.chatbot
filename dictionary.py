import random

sound={
    'a':1,
    'b':2,
    'c':3
}

for key in sound:
    print(key)

for value in sound.values():
    print(value)    

for key ,value in sound.items():
    print(key,value)

for count in range(5):
    x = random.randint(1,10)
    if x <= 4:
        attack ='a'
    elif x >= 4 and x <=6:
        attack ='b'
    else:
        attack = 'c'
    print(attack,' ',sound[attack])        
