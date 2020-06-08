import turtle
import time

win = turtle.Screen()
win.bgcolor("black")
win.setup(width = 600, height = 600)
win.title("Analogue Clock")
win.tracer(0)

#Create the drawing pen

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(hr, mn, sec, pen):

    #Drawing the clock
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    #Drawing hour hashes

    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for i in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
        #print(i)

    #Drawing the hands
        
    hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
    time_set = (hr, mn, sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])


while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    
    draw_clock(hr, mn, sec, pen)
    win.update()
    time.sleep(1)
    pen.clear()


win.mainloop()



