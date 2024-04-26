from tkinter import *
import random
Cchoice=["Rock","Paper","Scissor"]


root=Tk()
root.title("ROCK PAPER SCISSOR GAME-------------")
root.geometry("600x400")




counter=1
youwin=0
computerwin=0

screen=Entry(root,font=("arial",14),width=50,borderwidth=2)
screen.grid(row=2,column=0,columnspan=3,padx=10,pady=10)
com=Entry(root,font=("arial",14),width=50,borderwidth=2)
com.grid(row=1,column=0,columnspan=3,padx=10,pady=30)


def reset():
    global counter
    global youwin,computerwin
    counter = 1
    winner=Tk()
    winner.title("Winner Lobby")
    winner.geometry("500x300")
    win=Entry(winner,font=("arial",15),width=40,borderwidth=4)
    win.grid(row=0,column=0,columnspan=3,padx=10,pady=30)
    score=Entry(winner,font=("arial",15),width=40,borderwidth=4)
    score.grid(row=1,column=0,columnspan=3,padx=10,pady=30)

    if youwin>computerwin:
            win.insert(0,"You Win the game:")                
            score.insert(0,"Your score : "+str(youwin)+" Computer score : "+str(computerwin))
    elif computerwin>youwin:
            win.insert(0,"You Lose the game. Computer win the game:")    
            score.insert(0,"Your score : "+str(youwin)+" Computer score : "+str(computerwin))
    else:
            win.insert(0,"Match Drawn")    
            score.insert(0,"Your score : "+str(youwin)+" Computer score : "+str(computerwin))
    youwin=0
    computerwin=0
    clear_button=Button(winner,padx=10,pady=10,text="CLEAR",fg="#faa82d",bg="#2dfad4",command=clear)
    clear_button.grid(row=2,column=1)

def choose(user):
    global yourchoice
    global Computerchoice
    yourchoice=user
    Computerchoice=random.choice(Cchoice)
    screen.insert(0,"You choose "+user)
    screen.delete(0,END)
    com.delete(0,END)
    com.insert(0,"Computer choose "+Computerchoice)
    compare()

def compare():
    global counter,youwin,computerwin
    if yourchoice==Computerchoice:
        youwin+=1
        computerwin+=1
        screen.insert(0,"This Round is Drawn:")
    elif (yourchoice=="Paper" and Computerchoice=="Rock") or (yourchoice=="Rock" and Computerchoice=="Scissor") or (yourchoice=="Scissor" and Computerchoice=="Paper"):
        screen.insert(0,"you win this Round ")
        youwin+=1
    else:
        screen.insert(0,"Computer win this Round ")
        computerwin+=1
    counter+=1
    if counter>5:
        reset()



def clear():
    screen.delete(0,END)
    com.delete(0,END)

name=Label(root,text="ROCK PAPER SCISSOR GAME \n BEST OF SIX",pady=30)
rock_button=Button(root,padx=40,pady=20,text="ROCK",fg="#faa82d",bg="#2dfad4",command=lambda: choose("Rock"))
paper_button=Button(root,padx=40,pady=20,text="PAPER",fg="#faa82d",bg="#2dfad4",command=lambda: choose("Paper"))
scissor_button=Button(root,padx=40,pady=20,text="SCISSOR",fg="#faa82d",bg="#2dfad4",command=lambda: choose("Scissor"))
clear_button=Button(root,padx=10,pady=10,text="CLEAR",fg="#faa82d",bg="#2dfad4",command=clear)


name.grid(row=0,column=1)
rock_button.grid(row=3,column=0)
paper_button.grid(row=3,column=1)
scissor_button.grid(row=3,column=2)
clear_button.grid(row=4,column=1)

root.mainloop()