# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 01:16:08 2021

@author: Astitva
"""
import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

     
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 0.15
ball.dy = -0.15

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

Ascore = 0
Bscore = 0
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write("Player A: "+ str(Ascore)+"  Player B: "+str(Bscore), align="center", font=("Courier",18,"normal"))
    
#Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")
#Main game loop        
while True:
    win.update()
    #Move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #Border checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1
        Ascore +=1
        pen.clear()
        pen.write("Player A: "+ str(Ascore)+"  Player B: "+str(Bscore), align="center", font=("Courier",18,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
        Bscore+=1
        pen.clear()
        pen.write("Player A: "+ str(Ascore)+"  Player B: "+str(Bscore), align="center", font=("Courier",18,"normal"))
    #paddle hit
    if (ball.xcor() >340) and (ball.xcor()<350) and (ball.ycor()<(paddle_b.ycor()+40)) and (ball.ycor()> (paddle_b.ycor()-40)):
        ball.setx(340)
        ball.dx*=-1
        if ball.dx <0:
            ball.dx-=0.02
        else:
            ball.dx+=0.02
        if ball.dy <0:
            ball.dy-=0.02
        else:
            ball.dy+=0.02
        #print(ball.dx,ball.dy)
    if (ball.xcor() < -340) and (ball.xcor()>-350) and (ball.ycor()<(paddle_a.ycor()+40)) and (ball.ycor()> (paddle_a.ycor()-40)):
        ball.setx(-340)
        ball.dx*=-1
        if ball.dx <0:
            ball.dx-=0.02
        else:
            ball.dx+=0.02
        if ball.dy <0:
            ball.dy-=0.02
        else:
            ball.dy+=0.02
        #print(ball.dx,ball.dy)

    #endgame
    if Ascore== 7 :
        pen.clear()
        pen.write("Player A WINS !", align="center", font=("Courier",28,"normal"))
        turtle.exitonclick()
        break
    if Bscore== 7 :
        pen.clear()
        pen.write("Player B WINS!", align="center", font=("Courier",28,"normal"))
        turtle.exitonclick()
        break
