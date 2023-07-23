#pong
import turtle
import winsound

win = turtle.Screen() #window
win.title("pong game")
win.bgcolor("pink")
win.setup(width= 800, height= 600)
win.tracer(0) #have to manually update>>speeds up game

#pong A
pong_a = turtle.Turtle() #turtle object
pong_a.speed(0) #max speed
pong_a.shape("square")
pong_a.color("salmon4")
pong_a.shapesize(stretch_wid=5, stretch_len=1) #5x20=100 and 1x20=20
pong_a.penup() #no movement lines
pong_a.goto(-350,0) #minus for left side


#pong B 
pong_b = turtle.Turtle() #turtle object
pong_b.speed(0) #max speed
pong_b.shape("square")
pong_b.color("salmon4")
pong_b.shapesize(stretch_wid=5, stretch_len=1) #5x20=100 and 1x20=20
pong_b.penup() #no movement lines
pong_b.goto(350,0) #rightside


#movement_Functions
def pong_a_up(): #define function
    y = pong_a.ycor() 
    y +=20 #moves 20 pixels at y coordinate
    pong_a.sety(y) #sets y to new y

def pong_a_down(): 
    y = pong_a.ycor() 
    y -=20 
    pong_a.sety(y) 

def pong_b_up(): #define function
    y = pong_b.ycor() 
    y +=20 #moves 20 pixels at y coordinate
    pong_b.sety(y) #sets y to new y

def pong_b_down(): 
    y = pong_b.ycor() 
    y -=20 
    pong_b.sety(y)


#keybinds
win.listen() #listens for keyboard input
win.onkeypress(pong_a_up, "w") #lowercase 'w'
win.onkeypress(pong_a_down, "s") #lowercase 's'
win.onkeypress(pong_b_up, "Up") #uppercase- arrowkeys
win.onkeypress(pong_b_down, "Down") #uppercase- arrowkeys

#ball
ball= turtle.Turtle() #turtle object
ball.speed(0) #max speed
ball.shape("square")
ball.color("salmon4")
ball.penup() #no movement lines
ball.goto(0,0) #middle of screen
ball.dx = 0.05 #moves by x pixels---change numbers depending on pc speed
ball.dy = -0.05

#count
score_a= 0
score_b= 0

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("midnightblue")
pen.penup() #no movement lines
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B:0", align ="center", font=("Futura", 24, "normal"))

#loop
while True:
    win.update() #updates everytime loop runs

    #ball movement---loops 2 every movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #top and bottom borders---600/2=300 s0 290 pixels
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverses direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #left and right borders---800/2=400 so 390 pixels
    if ball.xcor() > 390:
        ball.goto(0,0) #returns back to centre
        ball.dx *= -1
        score_a +=1 #point for player A
        pen.clear() #clears scoreboard
        pen.write("Player A: {} Player B:{}".format(score_a, score_b), align ="center", font=("Futura", 24, "normal"))
        #updates score on screen^^

    if ball.xcor() < -390:
        ball.goto(0,0) #returns back to centre
        ball.dx *= -1
        score_b +=1 #point for player B
        pen.clear() #clears scoreboard
        pen.write("Player A: {} Player B:{}".format(score_a, score_b), align ="center", font=("Futura", 24, "normal"))
        #updates score on screen^^


    #pong ball hit
    #340 >edges---40s for top and bottom of pongs
    if (ball.xcor() > 340 and ball.xcor() <350 )and (ball.ycor() < pong_b.ycor() +40 and ball.ycor() > pong_b.ycor() -40):
       ball.setx(340)
       ball.dx *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < pong_a.ycor() +40 and ball.ycor() > pong_a.ycor() -40):
       ball.setx(-340)
       ball.dx *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

       

