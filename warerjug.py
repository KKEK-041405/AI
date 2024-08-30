print("Water Jug Problem")
x=int(input("Enter X:"))
y=int(input("Enter Y:"))
while True:
    rno=int(input("Enter the Rule No"))
    if rno==1: 
        if x<4:x=4
    if rno==2:
        if y<3:y=3
    if rno==5:
        if x>0:x=0
    if rno==6:
        if y>0:y=0
    if rno==7:
        if x+y>= 4 and y>0:x,y=4,y-(4-x)
    if rno==8:
        if x+y>=3 and x>0:x,y=x-(3-y),3
    if rno==9:
        if x+y<=4 and y>0:x,y=x+y,0
    if rno==10:
        if x+y<=3 and x>0:x,y=0,x+y
    print("X =" ,x)
    print("Y =" ,y)
    if (x==2):
        print(" The result is a Goal state")
        break

