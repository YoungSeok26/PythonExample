﻿data = ['a','b','c',['abcd','efg']]
print(data[0])
print(data[-1])
print(data[3][1])


a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']

print(b + c)

f = b * 3
print(f)

guest = ['a','b','c','d']
score = []
#score[78,85,62,49,98]
guest[0] = 'greenja2'
guest[1] = ['greenjoa1','greenjoa2']

#score[1:2] = ['greenjoa','greenjoa22']

#id=['kseok26','clown26','clown1126']
#passwd=['1234','5678','1q2w3e4r']
persondata = []

id = []
passwd = []

id.append('ksoeok26')
id.append('clown26')
id.append('clown1126')

passwd.append('1234')
passwd.append('5677')
passwd.append('1q2w3e4r')

name = []
tel = []

name.append('김영석')
name.append('김학성')
name.append('고광운')

tel.append('010-6472-2126')
tel.append('010-6274-2231')
tel.append('010-4880-4885')

for steps in range(3):
    print(steps)
    print(id[steps] + '  ' + passwd[steps] + '  ' + name[steps] + '  ' + tel[steps])


scores = [85,62,65,43,90,12,33,77,63]
scores.sort()
print(scores)
scores.reverse()
print(scores)

top5 = scores[0:5]
print(top5)


for i in data:
    if isinstance(i,list) :
        for j in i :
            print(j)
    else :
        print(i)
        
examextend = [85,63,63,45,90]
examextend.extend([50,53])
print(examextend)
examextend.append([12,34])
print(examextend)

t1 =()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('a','b'))
t6 = (1)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)