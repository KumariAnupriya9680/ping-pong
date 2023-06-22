import turtle
import winsound
import time
window = turtle.Screen()
window.title("ping pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)
#score
score_a= 0
score_b= 0
#paddle left
paddle_l= turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("blue")
paddle_l.penup()
paddle_l.goto(-350,0)
paddle_l.shapesize(stretch_wid=5,stretch_len=1)
#paddle right
paddle_r= turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("red")
paddle_r.penup()
paddle_r.goto(350,0)
paddle_r.shapesize(stretch_wid=5,stretch_len=1)
#the ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=0.2
ball.dy=0.2
#pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A :0 ,player B :0" , align="center" , font=("courier" ,24 ,"normal"))

#moving paddles
def paddle_l_Up():
    y=paddle_l.ycor()
    y=y+20
    paddle_l.sety(y)
def paddle_l_Down():
    y=paddle_l.ycor()
    y=y-20
    paddle_l.sety(y)
def paddle_r_Up():
    y=paddle_r.ycor()
    y=y+20
    paddle_r.sety(y)
def paddle_r_Down():
    y=paddle_r.ycor()
    y=y-20
    paddle_r.sety(y)

 #keyboard binding

window.listen()
window.onkeypress(paddle_l_Up ,"w")
window.onkeypress(paddle_l_Down ,"s")
window.onkeypress(paddle_r_Up ,"Up")
window.onkeypress(paddle_r_Down ,"Down")

 
    



while True:
    window.update()
    newx=ball.xcor() + ball.dx
    newy=ball.ycor() + ball.dy
    ball.setx(newx)
    ball.sety(newy)
    #border check
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy=ball.dy * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy=ball.dy * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor()> 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx=ball.dx * -1
    elif ball.xcor()<-390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx=ball.dx * -1
    if(-350< ball.xcor() < -340) and ball.ycor() <paddle_l.ycor() +50 and ball.ycor() >paddle_l.ycor() -50:
        ball.dx = ball.dx * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if(350> ball.xcor() > 340) and ball.ycor() <paddle_r.ycor() +50 and ball.ycor() >paddle_r.ycor() -50:
        ball.dx = ball.dx * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if(score_a == 5) or (score_b == 5):
        time.sleep(1)
        window.clear()
        if score_a > score_b:
            pen.color("black")
            pen.write("Player A won.", align="center", font=("courier", 24))
        else:
            pen.color("black")
            pen.write("Player B won.", align="center", font=("courier", 24))
        time.sleep(3)
        quit()
        


        
        
