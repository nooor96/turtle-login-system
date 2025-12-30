myusername = "Noor"
mypassword = "1260"
i=3
while i > 0:
    username= input("enter a username")
    password= input("enter a password")
    if mypassword == password and myusername == username :
        print("true - access log in ")
        import turtle

        t = turtle.Turtle()
        t.speed(4)
        t.width(4)
        t.penup()
        t.goto(-70, -80)
        t.pendown()
        t.begin_fill()
        for _ in range(2):
             t.forward(140)
             t.left(90)
             t.forward(110)
             t.left(90)
             t.end_fill()
        t.penup()
        t.goto(-40, 30)   
        t.setheading(0)
        t.pendown()

        t.left(90)
        t.forward(30)
        t.circle(40, 180)
        t.forward(30)
        t.penup()
        t.goto(0, -25)
        t.setheading(0)
        t.pendown()
        t.begin_fill()
        t.circle(8)
        t.end_fill() 
        turtle.done()
        break 
    else :
       i -= 1
       if i > 0 :
           print(f"wrong!{i}i left")
       else :
           print ("no access")
           import turtle
           t = turtle.Turtle()
           t.speed(4)
           t.width(4)
           t.penup()
           t.goto(-120, -60)
           t.pendown()
           t.fillcolor("black")
           t.begin_fill()
           for _ in range(2):
                t.forward(240)
                t.left(90)
                t.forward(120)
                t.left(90)
                t.end_fill()
           t.penup()
           t.goto(0, -15)
           t.color("red")
           t.pendown()
           t.write(
           "GAME OVER",
           align="center",
           font=("Arial", 24, "bold")
           )
           turtle.done()