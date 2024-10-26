#import necessary modules
import turtle
import pandas
loc = 'C:/Users/OYIBO Efetobor/Desktop/codes/day_25_us-states-game-start/us-states-game-start/'
screen = turtle.Screen()
screen.title('U.S STATES GAME')
img = loc+'blank_states_img.gif'
screen.addshape(img)
GAME_OVER_FONT = ("Ubuntu", 30, "normal")
STATE_FONT = ("Ubuntu", 15, "normal")
turtle.shape(img)
us_data = pandas.read_csv(loc+'50_states.csv')

read_x = us_data['x'].to_list()
read_y = us_data['y'].to_list()
read_states = us_data['state'].to_list()

def get_tuple():
    tuple_list =[]
    counter =0
    for i in read_x:
        my_tuple = (read_x[counter],read_y[counter])
        tuple_list.append(my_tuple)
        counter +=1
    return tuple_list

def get_location(state):
    i = 0
    for states in read_states:
        if state == states.lower():
            the_location = get_tuple()[i]
            return the_location
        else:
            i += 1


correct_guesses = []
counter = 0
score_board = turtle.Turtle()
    
score_board.hideturtle()
score_board.penup()
score_board.goto(0,300)

def update_score_board():
    score_board.clear()
    score_board.write(f"CURRENT SCORE: {counter}/50",align='center',font=GAME_OVER_FONT )
    
def answer():
    global counter, game_is_on
    
    update_score_board()
    answer_state1=screen.textinput(title=f'{counter}/50 states correct', prompt='what\'s another state\'s name?')
    
    answer_state2 = answer_state1.lower()
    if answer_state2 =='exit':
        game_is_on = False
    for i, state in  enumerate(read_states):
        if answer_state2 ==  state.lower():
            ans = turtle.Turtle()
            ans.hideturtle()
            ans.penup()
            ans.goto(get_location(answer_state2))
            ans.write(f'{answer_state2}',align='center',font=STATE_FONT)
            
            counter += 1
            return answer_state2
        else:
            pass

game_is_on = True  
        
while game_is_on:            
    correct_guesses.append(answer())
    
#states_to_learn.csv
remaining_states =[]
for i in read_states:
    if i.lower() not in correct_guesses:
        remaining_states.append(i)
        
#converting list to csv      
new_data = pandas.DataFrame(remaining_states)
new_data.to_csv('missing_states.csv')
    
    

      
turtle.mainloop()
