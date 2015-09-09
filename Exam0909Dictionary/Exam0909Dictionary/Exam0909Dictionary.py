#a={'name':'pey','phone':'01064722126','birth':'921126'}
#b=a.keys()
#print(b)

#b = list(a.keys())

#print(b)

#a={'name':'pey','phone':'01064722126','birth':'1126'}
#b=a.values()
#print(b)

#b=list(a.values())

#print(b)

#b=a.items()
#print(b)
#print(a.get('name'))
#print(a.get('age','24'))
#a.clear()

#movie = {'김영석':{'베테랑':'5점','암살':'4점','뷰티인사이드':'5점','앤트맨':'1점'},
#         '김학성':{'베테랑':'3점','암살':'5점','뷰티인사이드':'4점','앤트맨':'3점'},
#         '고광운':{'베테랑':'2점','암살':'4점','뷰티인사이드':'5점','앤트맨':'2점'}}

#print("홍길동의 영화평점:")
#print(movie.get('김영석'))

#print("고길동의 영화평점:")
#print(movie.get('김학성'))

#print("홍길동의 암살 영화 평점 : ")
#print(movie.get('김영석').get('암살'))

#s1=set([1,1,2,3,4,5,2,3,6])
#a=list(s1)
#print(a)

#answer= input()
#if answer.lower() == 'yes':
#    print("That will be an extra $10")

#print("Having a nice day")
#a=[(1,2),(3,4),(5,6)]

#for (first,last) in a :
#    print(first+last)
#for i in range(1,10):
#    for j in range(2,10):
#        print(str(j)+"*"+str(i),end="")
#        print("="+str(i*j),end="  ")
#    print("")

#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4) : 
#        turtle.forward(50)
#        turtle.right(90)

import turtle
sides = 7;
col = ['red','blue','black','green','yellow','purple','skyblue']
for steps in range(sides):
    turtle.color(col[steps])
    turtle.forward(100)
    turtle.right(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.right(360/sides)
