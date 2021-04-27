s1={0,1,2}
s2={1,2,3}
s3={2,3,4}
s4 ={i**3 for i in range(4)}

print(s4)



s_union = s1 | s2
print(s_union) #和集合

s_intersection = s1 & s2
print(s_intersection) #積集合

s_difference = s1 - s2
print(s_difference) #差集合

s_symmetric_difference = s1 ^ s2
print(s_symmetric_difference)#対称差集合






