#start ='hello'*8 +'¥n'
#middle = '!'*8 + '¥n'
#end ="Pythonの世界へ"

#print(start +middle +end)

#------

#mail = 'user-111@example.com'
#print(mail[9:-4])

#str ='1,2,3,4,5,6,7,8,9,10,100,1000'
#print(str.split(','))

#list =['僕の','名前は','ハイソン','と言います']
#join =''.join(list)
#print(join)
#------------------
#msg = 'こんばんはハイソンです'
#msg=msg.replace('こんばんは','調子はどう？')
#print(msg)
#--------------
#str ='美しい花が美しい庭に美しく咲いていました。'
#str =str.replace('美しい','とても美しい',10)
#print(str)
#-----------------
#print('こん{}は'.format('にち'))
#print('{1}は{0}です'.format('本日','10日'))
#print('{: .3f}'.format(1/3)) 0.333
#print('{:,}'.format(11111111111.123))

#print('身長は？')
#height=float(input('you >'))
#bmi =22
#weight=bmi * (height/100)**2
#print('身長が'+str(height)+'cmの場合の標準体重は',end='')
#print('{:.2f}kgです。'.format(weight))


#attacks =['a','b','c','d']
#attacks.append('e')
#numbers=[1,2,3,4,]
#n =min(len(numbers),len(attacks))
#for i in range(n):
#    print(str(numbers[i])+'<=='+attacks[i])
#print(attacks.pop(0))
#for num in range(5):
#    for attack in attacks:
#        print(attack,'',end="")
#    print()     
#    

#for num in range(1,6):
#    num_list.append(num)
#num_list =list[num for num in range(1,6) if num % 2 ==1]
#print(num_list)    

#scene=['attack1','attack2','attack3']
#attack = ['グランドストローク','スマッシュ','ボレー']
#sound = ['「ボッコーン」','「パコン」','「べキィ」']

#for scene,attack,sound in zip(scene,attack,sound):
#    print(scene,'攻撃->',attack,'（擬音）',sound)


#a =['a','b','c']
#for i in range(10):
#    print(a[0],a[1],a[2])

#onigiris =['おかか','さけ','ツナ','おかか','うめ','さけ']
#counts ={'おかか':0,'さけ':0,'ツナ':0,'うめ':0}

#for onigiri in onigiris:
#    counts[onigiri] += 1
#print(counts)    

#n = int(input('数> '))
#fac = 1
#for i in range(1,n+1) :
#    fac *= i
#print(str(n)+'! =',fac,sep=' ')

#n = int(input('数> '))
#for j in range(1,n+1):
#    print(str(j)+':',end='') # 改行しない出力
#    for i in range(0,j) :
#        print('■',end='')
#    print()  




#print() # 改行だけ出力
# Python3による別解45
#print(str(n)+':'+('■'*n))

#counter =0
#gokei = 0
#data =int(input('データ入力（負）'))

set1 ={1,2,3,4,5}
set2 ={3,4,5,6,7}

#print(set1 & set2)
#print(set1 | set2)

print(set1 - set2)





