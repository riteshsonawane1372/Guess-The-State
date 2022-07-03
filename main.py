import random as random
from turtle import Turtle,Screen
import turtle
import pandas



color_list=["red","brown","blue","pink","orange"]
my_screen = Screen()
my_turtle= Turtle()
image="./IndiaMap.gif"
my_screen.title("States In India")
my_screen.addshape(image)
#After adding the shape turtle can use it 
my_turtle.shape(image)
#read the data from pandas
data = pandas.read_csv("./india-states.csv")
all_States=list(data.state)

gussed_state=[]





while len(gussed_state) <33:
    answer_state = my_screen.textinput(title="State",prompt="Guess the State")
    if answer_state in all_States:
        gussed_state.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup
        t.write(answer_state)
        state_data=data[data.state==answer_state] # Getting hold of that row 
        t.goto(int(state_data.xcor),int(state_data.ycor))
        t.clear()
        t.color(random.choice(color_list))
        t.write(answer_state)
    my_screen.exitonclick()





















#! Below code was used to get the cor of x and y 
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # its an alternative for the screenExit 
