#import module
import turtle
import time
import random
from tkinter import *
from PIL import Image, ImageTk

#creating window1
wn = Tk()
wn.title("Snake game")
wn.geometry("600x600")
bg = ImageTk.PhotoImage(file = "python-bg.jpg")
lb1 = Label(wn, image = bg)
lb1.place(x = 0, y = 0)

#creating window2
def launch():
    global top
    top = Toplevel()
    wn.withdraw()
    top.geometry("600x600")
    top['bg'] = '#88a704'
    global l2
    #creating entry boxes
    l1 = Label(top, text = 'Enter user id: ',bg = '#88a704',font = 20)
    l1.grid(row = 50,column = 40,pady = 5)
    l2 = Entry(top, font = ('calibre',20))
    l2.grid(row = 50,column = 49,pady = 5)
    l6 = Label(top, text = 'Enter age: ',bg = '#88a704',font =20)
    l6.grid(row = 60,column = 40,pady = 5)
    l7 = Entry(top,font = ('calibre',20))
    l7.grid(row = 60,column = 49,pady = 5)
    l8 = Label(top, text = 'Enter country: ',bg = '#88a704',font =20)
    l8.grid(row = 70,column = 40,pady = 5)
    l9 = Entry(top, font = ('calibre',20))
    l9.grid(row = 70,column = 49,pady = 5)
    Button(top, text="CONTINUE", command=launch2,font = 24).grid(row =80,column = 50) 

#giving instructions        
def launch2():
    top.withdraw()
    global top1
    top1 = Toplevel()
    top1.geometry("600x600")
    top1['bg'] = '#88a704'
    name = l2.get()
    top1.title(name + "'s snake game ") 
    l3 = Label(top1,text ="How To Play:\n\nThe player controls a long, thin creature, resembling a snake, which roams around \non a bordered plane, picking up food, trying to avoid hitting its own tail or the edges \nof the playing area.\n\n Each time the snake eats a piece of food, its tail grows longer, \nthe score increases and its speed increases making the game increasingly difficult.\n\nThe user controls the direction of the snake's head and the snake's body follows.\nUse the keys:\nW or w (Up) \nA or a (Left)\nS or s(Down) \nD or d (Right) \n\nAll the best :)",bg ='#88a704',font = 20 ).grid()
    Button(top1, text="CONTINUE", command=launch3,font = 24).grid()
def close():
        top4.withdraw()

#creating snake game    
def launch3():
    top1.withdraw()
    window = turtle.Screen()
    turtle.setup(600,600)
    window.title('Snake Game')
    window.colormode(255)
    window.bgcolor(136,167,4)
    window.tracer(0)
    delay = 0.1
    # setting up the snake head
    the_snake = turtle.getturtle()
    the_snake.speed(0)
    the_snake.fillcolor('pink')
    the_snake.shape('square')
    the_snake.resizemode
    the_snake.turtlesize(1,1)
    the_snake.showturtle()
    the_snake.penup()
    the_snake.direction = "stop"
    #setting up the snake food
    snake_food = turtle.Turtle()
    snake_food.speed(0)
    snake_food.shape("square")
    snake_food.color("light blue")
    snake_food.turtlesize(1,1)
    snake_food.penup()
    snake_food.goto(0,100)
    snake_food.showturtle()
    snake_food = turtle.Turtle()
    snake_food.speed(0)
    snake_food.shape("square")
    snake_food.color("orange")
    snake_food.turtlesize(1,1)
    snake_food.penup()
    snake_food.goto(0,100)
    #score display
    score = 0
    High_Score = 0
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Times New Roman", 24, "bold"))
    #functions
    def go_up():
        if the_snake.direction != "down":
            the_snake.direction = "up"
    
    
    def go_down():
        if the_snake.direction != "up":
            the_snake.direction = "down"

    def go_left():
        if the_snake.direction != "right":
            the_snake.direction = "left"

    def go_right():
        if the_snake.direction != "left":
            the_snake.direction = "right"

    def move():
        if the_snake.direction == "up":
            y = the_snake.ycor()
            the_snake.sety(y + 20)

        if the_snake.direction == "down":
            y = the_snake.ycor()
            the_snake.sety(y - 20)

        if the_snake.direction == "left":
            x = the_snake.xcor()
            the_snake.setx(x - 20)

        if the_snake.direction == "right":
            x = the_snake.xcor()
            the_snake.setx(x + 20)
            
    #keyboard bindings
    window.listen()
    window.onkeypress(go_up, "w")
    window.onkeypress(go_up,"W")
    window.onkeypress(go_down, "s")
    window.onkeypress(go_down, "S")
    window.onkeypress(go_left, "a")
    window.onkeypress(go_left, "A")
    window.onkeypress(go_right, "d")
    window.onkeypress(go_right, "D")
    
    segments = []

#main game
    while True:
        window.update()

    #checking for collision with the border
        if the_snake.xcor()>290 or the_snake.xcor()<-290 or the_snake.ycor()>290 or the_snake.ycor()<-290:
            time.sleep(1)
            the_snake.goto(0,0)
            the_snake.direction = "stop"

        #hiding the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
        #clearing the segments list
            segments.clear()

        #reseting the score
            score = 0

        #reseting the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, High_Score), align="center", font=("Times New Roman", 12, "bold"))
            turtle.Screen().bye()
            global top4
            top4 = Toplevel()
            top4.title("Snake game")
            top4.geometry("600x600")
            bg = ImageTk.PhotoImage(file = "GAME-OVER.jpg")
            lb5 = Label(top4, image = bg)
            lb5.place(x = 0, y = 0)
            Button(top4, text="PLAY AGAIN",command = lambda: [close(), launch3()]).place(x=180, y=470) 
         
            

#check for a collision with the food
        if the_snake.distance(snake_food) < 20:
        #moving the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            snake_food.goto(x,y)

        #adding a body segment
            body_segment = turtle.Turtle()
            body_segment.speed(0)
            body_segment.shape("square")
            body_segment.color("purple")
            body_segment.penup()
            segments.append(body_segment)

        #shortening the delay
            delay -= 0.01

        #increasing the score
            score += 10

            if score > High_Score:
                High_Score = score
        
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, High_Score), align="center", font=("Times New Roman", 12, "bold"))

    #moving the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

    #moving segment 0 to where the head is
        if len(segments) > 0:
            x = the_snake.xcor()
            y = the_snake.ycor()
            segments[0].goto(x,y)
        move()    

    #checking for head collision with the body segments
        for segment in segments:
            if segment.distance(the_snake) < 20:
                time.sleep(1)
                the_snake.goto(0,0)
                the_snake.direction = "stop"
        
            #hiding the segments
                for segment in segments:
                    segment.goto(1000, 1000)
        
            #clearing the segments list
                segments.clear()

            #reseting the score
                score = 0

            #reseting the delay
                delay = 0.1
        
            #updating the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, High_Scoreigh_score), align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)

    window.mainloop()
   
Button(wn, text="CONTINUE", command=launch,font = 25).pack(pady=10)
wn.mainloop()