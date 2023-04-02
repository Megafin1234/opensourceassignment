import turtle
import random

myTurtle, tX,tY,tColor, tSize, tShape = [None]*6
shapelist=[]
playerTurtles=[]
swidth,sheight=500,500


turtle.title('거북리스트 활용')
turtle.setup(width=swidth+50,height=sheight+50 )
turtle.screensize(swidth,sheight)
shapelist = turtle.getshapes()
for i in range (0,100) :
    random.shuffle(shapelist)
    myTurtle= turtle.Turtle(shapelist[0])
    tX = random.randrange(-swidth/2,swidth/2)
    tY = random.randrange(-sheight/2,sheight/2)
    r= random.random(); g= random.random(); b=random.random()
    tSize=random.randrange(1,3)
    playerTurtles.append([myTurtle,tX,tY,tSize,r,g,b])
        
for tlist in playerTurtles:
    myTurtle = tlist[0]
    myTurtle.color((tlist[4],tlist[5],tlist[6]))
    myTurtle.pencolor((tlist[4],tlist[5],tlist[6]))
    myTurtle.turtlesize(tlist[3])
    myTurtle.goto(tlist[1],tlist[2])
turtle.done()