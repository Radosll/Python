import turtle
#angles walls
a = (90)
h = (80)
i = (170)
#angles roof
b = (60)
c = (120)
g = (30)
j = (50)
k = (110)
#walls
d = (150)
#roof
e = (150)
f = (200)
#shape
turtle.shape('turtle')
#speed
turtle.speed(100)
#color
turtle.pencolor('green')
turtle.fillcolor('orange')



turtle.begin_fill()
#walls 1
turtle.forward(d)
turtle.right(a)

turtle.forward(d)
turtle.right(a)

turtle.forward(d)
turtle.right(a)

turtle.forward(d)
turtle.right(a)
#roof
turtle.left(b)
turtle.forward(e)
#
turtle.right(j)
turtle.forward(f)

turtle.rt(70)
turtle.fd(150)
turtle.rt(30)
turtle.fd(150)
turtle.rt(80)
turtle.fd(200)
turtle.rt(100)
turtle.fd(150)

turtle.lt(30)
turtle.fd(150)
turtle.rt(110)
turtle.fd(200)
turtle.rt(70)
turtle.fd(150)
turtle.rt(110)
turtle.fd(200)
turtle.end_fill()
turtle.lt(80)
turtle.fd(150)
#door
turtle.color('brown')
turtle.begin_fill()
turtle.right(90)
turtle.forward(50)
turtle.right(a)
turtle.forward(35)
turtle.left(a)
turtle.forward(20)
turtle.left(a)
turtle.forward(35)
turtle.end_fill()



turtle.exitonclick()


#Create by Rado T. 14319 for eng. V. Nachev