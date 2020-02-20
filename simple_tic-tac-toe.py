import tkinter as tk

def players(frame1):
    
    global name1, name2
    
    label1 = tk.Label(frame1, text = '1st Players Name :')
    label2 = tk.Label(frame1, text = '2nd Players Nmae :')
    label1.grid(row = 0, column = 0, pady = 5)
    label2.grid(row = 1, column = 0, pady = 5)
    
    entry1 = tk.Entry(frame1, textvariable = name1)
    entry2 = tk.Entry(frame1, textvariable = name2)
    entry1.grid(row = 0, column = 1, pady = 5)
    entry2.grid(row = 1, column = 1, pady = 5)


    
        
def ButtonClicked(button):
    
    global clicked, listOfButtons
    
    if button['text'] == "" and clicked == True:
        button['text'] = 'X'
        clicked = False
        
        listOfButtons.remove(button)
        
        checkForWin_X()
        
        if len(listOfButtons) == 0:
            disable()
        
    elif button['text'] == "" and clicked == False:
        button['text'] = '0'
        clicked = True
                
        listOfButtons.remove(button)
        
        checkForWin_O()
              
def checkForWin_X():
    
    print(pos_1['text'])
    if (pos_1['text'] == 'X' and pos_2['text'] == 'X' and pos_3['text'] == 'X' or
        pos_4['text'] == 'X' and pos_5['text'] == 'X' and pos_6['text'] == 'X' or
        pos_7['text'] == 'X' and pos_8['text'] == 'X' and pos_9['text'] == 'X' or
        pos_1['text'] == 'X' and pos_4['text'] == 'X' and pos_7['text'] == 'X' or
        pos_3['text'] == 'X' and pos_6['text'] == 'X' and pos_9['text'] == 'X' or
        pos_3['text'] == 'X' and pos_5['text'] == 'X' and pos_7['text'] == 'X' or
        pos_1['text'] == 'X' and pos_5['text'] == 'X' and pos_9['text'] == 'X' or
        pos_2['text'] == 'X' and pos_5['text'] == 'X' and pos_8['text'] == 'X'):
        
        print('x Wins')
        text = 'Congrats ' + name1.get() + ' you Won !!'
        tk.messagebox.showinfo('tk', text)
        disable()
    
def checkForWin_O():    
    
    if (pos_1['text'] == '0' and pos_2['text'] == '0' and pos_3['text'] == '0' or
        pos_4['text'] == '0' and pos_5['text'] == '0' and pos_6['text'] == '0' or
        pos_7['text'] == '0' and pos_8['text'] == '0' and pos_9['text'] == '0' or
        pos_1['text'] == '0' and pos_4['text'] == '0' and pos_7['text'] == '0' or
        pos_3['text'] == '0' and pos_5['text'] == '0' and pos_7['text'] == '0' or
        pos_3['text'] == '0' and pos_6['text'] == '0' and pos_9['text'] == '0' or
        pos_1['text'] == '0' and pos_5['text'] == '0' and pos_9['text'] == '0' or
        pos_2['text'] == '0' and pos_5['text'] == '0' and pos_8['text'] == '0'):
        
        print('0 Wins')
        text = 'Congrats ' + name2.get() + ' you Won !!'
        tk.messagebox.showinfo('tk', text)
        disable()
        
def disable():
    
    Buttons = [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9]
    for button in Buttons:
        button.configure(state = tk.DISABLED)
       
if __name__ == '__main__':    
    
    root = tk.Tk()
    
    root.title('Tic Tac Toe')
    
    frame1 = tk.Frame(root)
    frame1.grid(sticky = tk.N, padx = 10, pady = 10)
    
    frame2 = tk.Frame(root)
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
    

    