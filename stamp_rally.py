import random
station_all = {0, 1, 2, 3, 4} # 全5駅  #{}は、set
counter = {1:0, 2:0, 3:0, 4:0} #最後の1駅になった回数の各駅のカウント　＃辞書
for num in range(10000):
    station_current = 0 # スタートは0から
    station_arrived = {0} # スタンプゲットした駅
    while len(station_arrived) < 4 :
        randomcoin = random.randint(0,1)*2-1
        station_current += randomcoin
        if station_current == -1:
            station_current = 4
        elif station_current == 5:
            station_current = 0
        station_arrived.add(station_current)
    i = list(station_all - station_arrived)[0] #差集合
    x = counter[i]
   # print(counter)
    counter[i] = counter[i] +1
   #if num % 100000 == 0:
#print(station_current)   
print(counter)
