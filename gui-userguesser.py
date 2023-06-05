
import tkinter as tk
import random
class Guessg:
    score=100
    def __init__(self):
        global answer
        start=int(Starting_Number_entry.get())
        end=int(Ending_Number_entry.get())
        answer=random.randint(start,end)
        Result_label.config(text="Result")
        Hint_label.config(text="Hint")
    def get_guess():
        while True:
            try:
                guess=int(Guess_Number_entry.get())
                return guess
            except ValueError:
                Result_label.config(text="Result: " + "Invalid input. Please input a number")
    def check_guess(guess,answer):
        if guess==answer:
            return True
        else:
            return False
    def give_hint(guess,answer):
        if guess<answer:
            Hint_label.config(text="Hint: " + "The number is higher than your guess.")
        else:
            Hint_label.config(text="Hint: " + "The number is lower than your guess")
    def play_game():
        guess=Guessg.get_guess()
        if Guessg.check_guess(guess,answer):
            Result_label.config(text="Result: " + "Congratulations you guessed the number")
            Score_label.config(text="Score: "+str(Guessg.score))
        else:
            Guessg.give_hint(guess,answer)
            Guessg.score-=10
        
root=tk.Tk()
root.title("Guessing Game")
root.geometry("700x700")

back = tk.Frame(master=root, bg='black', highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
back.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

Starting_Number_label=tk.Label(back,text="Starting Number: \t\t\t\t\t", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Starting_Number_label.pack()
Starting_Number_entry=tk.Entry(back, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
Starting_Number_entry.pack()

Ending_Number_label=tk.Label(back,text="Ending Number: \t\t\t\t\t", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Ending_Number_label.pack()
Ending_Number_entry=tk.Entry(back, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
Ending_Number_entry.pack()

Generate_button=tk.Button(back,text="Generate rand num",command=Guessg)
Generate_button.pack()


Guess_Number_label=tk.Label(back,text="Guess Number: \t\t\t\t\t", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Guess_Number_label.pack()
Guess_Number_entry=tk.Entry(back, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
Guess_Number_entry.pack()


submit_button=tk.Button(back,text="Check num",command=Guessg.play_game,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
submit_button.pack()

Hint_label=tk.Label(back,text="Hint", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Hint_label.pack()

Result_label=tk.Label(back,text="Result", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Result_label.pack()

Score_label=tk.Label(back,text="Score", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Score_label.pack()

def close_window():
    root.destroy()

action = tk.Button (master = back, text = "Close", command = close_window,bg = '#ADD8E6', padx = '10', pady = '5',height = ' 1', width = '10')
action.pack()
root.mainloop()