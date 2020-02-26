########################################################################
##################   Tic tac toe using tkinter   #######################
########################################################################

########################################################################
########################################################################

###############   structure of game    #######################

##################    1 | 2 | 3   ############################
##################   -----------  ############################
##################    4 | 5 | 6   ############################
##################   -----------  ############################
##################    7 | 8 | 9   ############################

########################################################################
########################################################################





import tkinter as tk

def players(frame1) -> 'function to take players name as an input':
    
    global name1, name2 
    ## Both name1 and name2 are defined at the bottom as string varriables
    
    label1 = tk.Label(frame1, text = '1st Players Name :')
    label2 = tk.Label(frame1, text = '2nd Players Nmae :')
    label1.grid(row = 0, column = 0, pady = 5)
    label2.grid(row = 1, column = 0, pady = 5)
    
    entry1 = tk.Entry(frame1, textvariable = name1)
    entry2 = tk.Entry(frame1, textvariable = name2)
    entry1.grid(row = 0, column = 1, pady = 5)
    entry2.grid(row = 1, column = 1, pady = 5)


    
        
def ButtonClicked(button: 'button referrs to the button which was recently clicked') ->'''Whenever any
    button is clicked this function will be called''':
    
    global clicked ##  clicked is true for X and false for O 
    global listOfButtons  ## listOfButtons is a list which contains all buttons as an elements
    
    if button['text'] == "" and clicked == True: # For First player
        button['text'] = 'X'
        clicked = False  
        # After replacing clicked button by X Clicked will become false for second players turn
        
        listOfButtons.remove(button)
        # removing the button which is named recently from the listOfButtons
        checkForWin_X() # Checking for the winner Each time whenever any changes occur
        
        if len(listOfButtons) == 0: # When listOfButtons is empty, disable all buttons
            disable()
        
    elif button['text'] == "" and clicked == False: # For Second Player
        button['text'] = '0'
        clicked = True
        # After replacing clicked button by O Clicked will become True for First players turn

        listOfButtons.remove(button)
        # removing the button which is named recently from the listOfButtons

        checkForWin_O() # Checking for the winner Each time whenever any changes occur
              
def checkForWin_X() -> 'This Function checks for win whenever any chang is made by player1':
    
    print(pos_1['text'])
    if (pos_1['text'] == 'X' and pos_2['text'] == 'X' and pos_3['text'] == 'X' or
        pos_4['text'] == 'X' and pos_5['text'] == 'X' and pos_6['text'] == 'X' or
        pos_7['text'] == 'X' and pos_8['text'] == 'X' and pos_9['text'] == 'X' or
        pos_1['text'] == 'X' and pos_4['text'] == 'X' and pos_7['text'] == 'X' or
        pos_3['text'] == 'X' and pos_6['text'] == 'X' and pos_9['text'] == 'X' or
        pos_3['text'] == 'X' and pos_5['text'] == 'X' and pos_7['text'] == 'X' or
        pos_1['text'] == 'X' and pos_5['text'] == 'X' and pos_9['text'] == 'X' or
        pos_2['text'] == 'X' and pos_5['text'] == 'X' and pos_8['text'] == 'X'):

        # These are all the Possible conditions for winning the game 
        # if any one condition matches the player will win

        print('x Wins')
        text = 'Congrats ' + name1.get() + ' you Won !!'
        tk.messagebox.showinfo('tk', text) # Messagebox will pop out with winner name
        disable() ## Disabling all the buttons when any player wins
    
def checkForWin_O() -> 'This Function checks for win whenever any chang is made by player2':
    
    if (pos_1['text'] == '0' and pos_2['text'] == '0' and pos_3['text'] == '0' or
        pos_4['text'] == '0' and pos_5['text'] == '0' and pos_6['text'] == '0' or
        pos_7['text'] == '0' and pos_8['text'] == '0' and pos_9['text'] == '0' or
        pos_1['text'] == '0' and pos_4['text'] == '0' and pos_7['text'] == '0' or
        pos_3['text'] == '0' and pos_5['text'] == '0' and pos_7['text'] == '0' or
        pos_3['text'] == '0' and pos_6['text'] == '0' and pos_9['text'] == '0' or
        pos_1['text'] == '0' and pos_5['text'] == '0' and pos_9['text'] == '0' or
        pos_2['text'] == '0' and pos_5['text'] == '0' and pos_8['text'] == '0'):
        
        # These are all the Possible conditions for winning the game 
        # if any one condition matches the player will win

        print('0 Wins')
        text = 'Congrats ' + name2.get() + ' you Won !!'
        tk.messagebox.showinfo('tk', text) # Messagebox will pop out with winner name
        disable()  ## Disabling all the buttons when any player wins
        
def disable() -> "This function is used to disable all the buttons":
    
    Buttons = [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9]
    # Button is a list with all the buttons as its elements
    
    for button in Buttons:
        button.configure(state = tk.DISABLED)
       
if __name__ == '__main__':    
    
    root = tk.Tk() # Making root as an instance of Tk() class
    
    root.title('Tic Tac Toe')
    
    frame1 = tk.Frame(root)  # Frame1 is foe names of the players 
    frame1.grid(sticky = tk.N, padx = 10, pady = 10)
    
    frame2 = tk.Frame(root) # frame2 is to create matrix of buttons  
    frame2.grid(sticky = tk.S)
    
    clicked = True
    name1 = tk.StringVar()
    name2 = tk.StringVar()
    
    players(frame1)
    
    
    pos_1 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_1))
    pos_1.grid(row = 0, column = 0, padx = 1, pady = 1)
    pos_2 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_2))
    pos_2.grid(row = 0, column = 1, padx = 1, pady = 1)
    pos_3 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_3))
    pos_3.grid(row = 0, column = 2, padx = 1, pady = 1)
    pos_4 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_4))
    pos_4.grid(row = 1, column = 0, padx = 1, pady = 1)
    pos_5 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_5))
    pos_5.grid(row = 1, column = 1, padx = 1, pady = 1)
    pos_6 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_6))
    pos_6.grid(row = 1, column = 2, padx = 1, pady = 1)
    pos_7 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_7))
    pos_7.grid(row = 2, column = 0, padx = 1, pady = 1)
    pos_8 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_8))
    pos_8.grid(row = 2, column = 1, padx = 1, pady = 1)
    pos_9 = tk.Button(frame2, text = "", bg = "#706c61", height = 4, width = 10, fg = 'white', command = lambda: ButtonClicked(pos_9))
    pos_9.grid(row = 2, column = 2, padx = 1, pady = 1)
    
    listOfButtons = [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9]
    
    root.mainloop()
    

    