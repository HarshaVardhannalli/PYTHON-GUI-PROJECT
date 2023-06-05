
import tkinter as tk
import random
class Us:
    us=0
class Ss(Us):
    ss=0
class rps(Ss):
    turn=3
    def sys_turnr():
        x=random.randint(1,3)
        if rps.turn>0:
            if x==3:
                system.config(text="SYSTEM Choice: SCISSOR")
                Us.us+=1
                uscore.config(text=f"User Score:{Us.us}")
                rps.turn-=1
            elif x==2:
                system.config(text="SYSTEM Choice: PAPER")
                Ss.ss+=1
                sscore.config(text=f"System Score:{Ss.ss}")
                rps.turn-=1
            else:
                rps.turn-=1
                Us.us+=1
                Ss.ss+=1
                system.config(text="SYSTEM Choice: ROCK")
                uscore.config(text=f"User Score:{Us.us}")
                sscore.config(text=f"System Score:{Ss.ss}")
        if rps.turn==0:
            rps.dis()
    def sys_turnp():
        x=random.randint(1,3)
        if rps.turn>0:
            if x==1:
                system.config(text="SYSTEM Choice: ROCK")
                Us.us+=1
                uscore.config(text=f"User Score:{Us.us}")
                rps.turn-=1
            elif x==3:
                system.config(text="SYSTEM Choice: SCISSOR")
                Ss.ss+=1
                sscore.config(text=f"System Score:{Ss.ss}")
                rps.turn-=1
            else:
                rps.turn-=1
                Us.us+=1
                Ss.ss+=1
                system.config(text="SYSTEM Choice: PAPER")
                uscore.config(text=f"User Score:{Us.us}")
                sscore.config(text=f"System Score:{Ss.ss}")
        if rps.turn==0:
            rps.dis()
    def sys_turns():
        x=random.randint(1,3)
        if rps.turn>0:
            if x==2:
                system.config(text="SYSTEM Choice: PAPER")
                Us.us+=1
                uscore.config(text=f"User Score:{Us.us}")
                rps.turn-=1
            elif x==1:
                system.config(text="SYSTEM Choice: ROCK")
                Ss.ss+=1
                sscore.config(text=f"System Score:{Ss.ss}")
                rps.turn-=1
            else:
                rps.turn-=1
                Us.us+=1
                Ss.ss+=1
                system.config(text="SYSTEM Choice: SCISSOR")
                uscore.config(text=f"User Score:{Us.us}")
                sscore.config(text=f"System Score:{Ss.ss}")
        if rps.turn==0:
            rps.dis()
            
    def dis():
        if Us.us>Ss.ss:
            result.config(text="RESULT: You won the game")
        elif Ss.ss>Us.us:
            result.config(text="RESULT: System has won")
        else:
            result.config(text="RESULT: It's a TIE")
    def starta():
        Us.us=0
        Ss.ss=0
        rps.turn=3
        uscore.config(text="User Score: 0")
        sscore.config(text="System Score: 0")
        result.config(text="RESULT:")
        
        
root=tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("700x700")

back = tk.Frame(master=root, bg='black', highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
back.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

system=tk.Label(back,text="SYSTEM Choice:", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
system.pack()
user=tk.Label(back,text="Your Choice:", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
user.pack()
rock=tk.Button(back,text="ROCK",command=rps.sys_turnr,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
rock.pack()
paper=tk.Button(back,text="PAPER",command=rps.sys_turnp,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
paper.pack()
scissor=tk.Button(back,text="SCISSOR",command=rps.sys_turns,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
scissor.pack()
result=tk.Label(back,text="Result:", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
result.pack()
uscore=tk.Label(back,text="User Score:0", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
uscore.pack()
sscore=tk.Label(back,text="Sytem Score:", bg='black',font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
sscore.pack()
Start=tk.Button(back,text="START AGAIN",command=rps.starta,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
Start.pack()
def close_window():
    root.destroy()

action = tk.Button (master = back, text = "Close", command = close_window,bg = '#ADD8E6', padx = '10', pady = '5',height = ' 1', width = '10')
action.pack()
root.mainloop()