#isa Grace Guthrie and Ellen Kevin
#part 1
import turtle
jack=turtle.Turtle()
jack.color("yellow")
for side in range(4):
    if side == 2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)

#isa Grace Guthrie and Ellen Kevin
#part 1.2
import turtle
jack=turtle.Turtle()
jack.color("yellow")
for side in range(4):
    if side == 3:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)

#isa Grace Guthrie and Ellen Kevin
#part 1.3
import turtle
jack=turtle.Turtle()
jack.color("yellow")
for side in range(4):
    if side == 2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)

#Isa Grace guthrie and Ellen Kevin
#part 2
import turtle
jack=turtle.Turtle()
jack.color("yellow")
for side in range(4):
    jack.forward(100)
    jack.right(90)
    if side == 1:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)
    if side== 2:
        jack.color("green")
    jack.forward(100)
    jack.right(90)
    if side==3:
        jack.color("pink")
    jack.forward(100)
    jack.right(90)

#isa Grace Guthrie and Ellen Kevin
#part 3
import math
for x in range(2,11):
    print(x)
    if x%2==1:
        print("odd")
    if x%2==0:
        print("even")

#the authors names are Isa Grace Guthrie and Ellen Kevin
#part 4
import turtle
romeo=turtle.Turtle()
juliet=turtle.Turtle()
juliet.color("misty rose")
juliet.width(3)
romeo.color("violet")
romeo.width("3")
romeo_last_name="montague"
romeo.left(40)
romeo.forward(100)
for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()
if romeo_last_name=="montague":
    juliet.left(140)
    juliet.forward(100)
    for side in range(185):
        juliet.forward(1)
        juliet.right(1)
    juliet.hideturtle()

#the authors names are Isa Grace Guthrie and Ellen Kevin
#part 5
elements=["paper","rock","paper","scissor","rock","scissor","paper"]
for x in elements:
    if x=="paper":
        print("paper eats rock")
    if x=="rock":
        print("rock hits scissor")
    if x=="scissor":
        print("scissor beats paper")
