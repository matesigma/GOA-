from turtle  import *
#we want to paint house
#step 1:draw square
speed(10)
width(7)

color ("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square

#drawing a door
 
begin_fill()

forward (70)
color("yellow")
left (90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


begin_fill()
left(30)
penup()
forward(70)
left(90)
pendown()
color("brown")
forward(70)
left(90)
forward(70)
end_fill()


begin_fill()
right(90)
penup()
forward(130)
right(90)
forward(70)
right(90)
pendown()
forward(80)
right(90)
forward(70)
end_fill()

exitonclick()

