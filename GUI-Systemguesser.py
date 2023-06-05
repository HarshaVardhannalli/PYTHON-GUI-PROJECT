
import tkinter as tk
import random
class sysg:
    def __init__(self):
        start=int(Starting_Number_entry.get())
        end=int(Ending_Number_entry.get())
        sys_out.config(text="Select a number between {0} and {1} \nThen divide it by 2 and multiply it by 3, add 4 and subtract 5\n Finally enter your result below".format(start,end))
    def result():
        y=float(userin_entry.get())
        x=(y+1)*2/3
        final_out.config(text="Your Number is {0}".format(x))
        
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

Ending_Number_label=tk.Label(back,text="Ending Number: \t\t\t\t\t", bg='black', font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
Ending_Number_label.pack()
Ending_Number_entry=tk.Entry(back, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
Ending_Number_entry.pack()

button2=tk.Button(back,text="Start",command=sysg,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
button2.pack()

sys_out=tk.Label(back,text="Step to follow", bg='black', font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
sys_out.pack()

userin=tk.Label(back,text="Your Result", bg='black', font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
userin.pack()
userin_entry=tk.Entry(back, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
userin_entry.pack()

button1=tk.Button(back,text="SUBMIT", command=sysg.result,bg = '#ADD8E6', padx = '15', pady = '10',height = ' 1', width = '10')
button1.pack()

final_out=tk.Label(back,text="Final Output", bg='black', font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue')
final_out.pack()

def close_window():
    root.destroy()

action = tk.Button (master = back, text = "Close", command = close_window,bg = '#ADD8E6', padx = '10', pady = '5',height = ' 1', width = '10')
action.pack()
root.mainloop()