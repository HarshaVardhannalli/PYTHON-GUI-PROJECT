
import tkinter as tk
import numpy as np
class SFl:
    sfl=np.empty(0)
class UFl(SFl):
    ufl=np.empty(0)
class SWin(UFl):
    s5=0
class UWin(SWin):
    u5=0
class Sys(UWin):
    sys=np.empty(0)
class bingo(Sys):
    usa=np.empty(0)
    def start():
        bingo.sysslip()
        x=np.arange(1,26)
        frame1 = tk.Frame(root)
        l1=tk.Label(frame1, textvariable=u1,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=0,column=0)     
        l2=tk.Label(frame1,textvariable=u2,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=0,column=1)       
        l3=tk.Label(frame1,textvariable=u3,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=0,column=2)       
        l4=tk.Label(frame1,textvariable=u4,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=0,column=3)                   
        l5=tk.Label(frame1,textvariable=u5,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=0,column=4)                
        l6=tk.Label(frame1,textvariable=u6,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=1,column=0)                    
        l7=tk.Label(frame1,textvariable=u7,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=1,column=1)                   
        l8=tk.Label(frame1,textvariable=u8,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=1,column=2)                   
        l9=tk.Label(frame1,textvariable=u9,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=1,column=3)                 
        l10=tk.Label(frame1,textvariable=u10,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=1,column=4)                 
        l11=tk.Label(frame1,textvariable=u11,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=2,column=0)                  
        l12=tk.Label(frame1,textvariable=u12,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=2,column=1)                   
        l13=tk.Label(frame1,textvariable=u13,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=2,column=2)                  
        l14=tk.Label(frame1,textvariable=u14,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=2,column=3)                    
        l15=tk.Label(frame1,textvariable=u15,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=2,column=4)                 
        l16=tk.Label(frame1,textvariable=u16,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=3,column=0)                 
        l17=tk.Label(frame1,textvariable=u17,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=3,column=1)                  
        l18=tk.Label(frame1,textvariable=u18,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=3,column=2)                   
        l19=tk.Label(frame1,textvariable=u19,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=3,column=3)                   
        l20=tk.Label(frame1,textvariable=u20,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=3,column=4)                  
        l21=tk.Label(frame1,textvariable=u21,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=4,column=0)                   
        l22=tk.Label(frame1,textvariable=u22,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=4,column=1)                  
        l23=tk.Label(frame1,textvariable=u23,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=4,column=2)                    
        l24=tk.Label(frame1,textvariable=u24,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=4,column=3)            
        l25=tk.Label(frame1,textvariable=u25,bg = '#ADD8E6', padx = '15', pady = '10', height = ' 1', width = '5').grid(row=4,column=4)
        frame1.pack()
        frame5=tk.Frame(root)
        U_result=tk.Label(frame5, textvariable =rs, font = ('Times New Roman', 15), pady = '15', padx = '80', fg = 'Blue').pack(side = 'left')
        S_result=tk.Label(frame5, textvariable =srs, font = ('Times New Roman', 15), pady = '15', padx = '80', fg = 'Blue').pack(side = 'left')
        frame5.pack(pady = '15')
    
    def Playagain():
        Sys.sys=np.empty(0)
        bingo.usa=np.empty(0)
        frame6=tk.Frame(root)
        tk.Button(frame6,text='Play Again',bg = '#ADD8E6', padx = '15', pady = '10', command =bingo.sysslip, height = ' 1', width = '10').pack(side = 'top', padx = '15')
        action = tk.Button (frame6, text = "Close", command = close_window,bg = '#ADD8E6', padx = '10', pady = '5',height = ' 1', width = '10')
        action.pack()
        frame6.pack(pady = '15')
        
    def sysslip():
        rs.set("RESULT:")
        srs.set("SYSTEM RESULT:")
        x=np.arange(1,26)
        for i in range(25):
            y=np.random.choice(x,size=1)
            Sys.sys=np.append(Sys.sys,int(y))
            x=np.delete(x,np.where(x==y))
        x=np.arange(1,26)
        for i in range(25):
            y=np.random.choice(x,size=1)
            bingo.usa=np.append(bingo.usa,int(y))
            x=np.delete(x,np.where(x==y))
        bingo.val_upd()
    def Choice():
        u_choice=int(choice.get())
        if u_choice>25 or u_choice==0:
            rs.set("ENTER NUMBER BELOW 25 except 0")
        elif u_choice<=25 and u_choice not in bingo.usa:
            rs.set("THAT NUMBER IS ALREADY OVER")
        else:
            bingo.usa[bingo.usa==u_choice]=0
            Sys.sys[Sys.sys==u_choice]=0
            s_choice=np.random.choice(Sys.sys[Sys.sys>0])
            sc.set(f"System Choice : {s_choice}")
            bingo.usa[bingo.usa==s_choice]=0
            bingo.val_upd()
            Sys.sys[Sys.sys==s_choice]=0
            bingo.win_check()
        
    def win_check():
        winu=bingo.usa.reshape(5,5)
        wins=Sys.sys.reshape(5,5)
        for i in range(5):
            if np.add.reduce(winu[i])==0 and i not in UFl.ufl:
                UFl.ufl=np.append(UFl.ufl,int(i))
                UWin.u5+=1
                if UWin.u5==5:
                    rs.set("RESULT: BINGO YOU HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif UWin.u5==4:
                    rs.set("RESULT: YOU NEED ONE MORE LINE TO WIN")
                elif UWin.u5==3:
                    rs.set("RESULT: YOU NEED TWO MORE LINES TO WIN")
                elif UWin.u5==2:
                    rs.set("RESULT: YOU NEED THREE MORE LINES TO WIN")
                elif UWin.u5==1:
                    rs.set("RESULT: YOU NEED FOUR MORE LINES TO WIN")
            if winu[0][0]==0 and winu[1][1]==0 and winu[2][2]==0 and winu[3][3]==0 and winu[4][4]==0 and 7 not in UFl.ufl:
                UWin.u5+=1
                UFl.ufl=np.append(UFl.ufl,7)
                if UWin.u5==5:
                    rs.set("RESULT: BINGO YOU HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif UWin.u5==4:
                    rs.set("RESULT: YOU NEED ONE MORE LINE TO WIN")
                elif UWin.u5==3:
                    rs.set("RESULT: YOU NEED TWO MORE LINES TO WIN")
                elif UWin.u5==2:
                    rs.set("RESULT: YOU NEED THREE MORE LINES TO WIN")
                elif UWin.u5==1:
                    rs.set("RESULT: YOU NEED FOUR MORE LINES TO WIN")
            if winu[0][4]==0 and winu[1][3]==0 and winu[2][2]==0 and winu[3][1]==0 and winu[4][0]==0 and 8 not in UFl.ufl:
                UWin.u5+=1
                UFl.ufl=np.append(UFl.ufl,8)
                if UWin.u5==5:
                    rs.set("RESULT: BINGO YOU HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif UWin.u5==4:
                    rs.set("RESULT: YOU NEED ONE MORE LINE TO WIN")
                elif UWin.u5==3:
                    rs.set("RESULT: YOU NEED TWO MORE LINES TO WIN")
                elif UWin.u5==2:
                    rs.set("RESULT: YOU NEED THREE MORE LINES TO WIN")
                elif UWin.u5==1:
                    rs.set("RESULT: YOU NEED FOUR MORE LINES TO WIN")
            if winu[0][i]==0 and winu[1][i]==0 and winu[2][i]==0 and winu[3][i]==0 and winu[4][i]==0 and i+9 not in UFl.ufl:
                UWin.u5+=1
                UFl.ufl=np.append(UFl.ufl,int(i+9))
                if UWin.u5==5:
                    rs.set("RESULT: BINGO YOU HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif UWin.u5==4:
                    rs.set("RESULT: YOU NEED ONE MORE LINE TO WIN")
                elif UWin.u5==3:
                    rs.set("RESULT: YOU NEED TWO MORE LINES TO WIN")
                elif UWin.u5==2:
                    rs.set("RESULT: YOU NEED THREE MORE LINES TO WIN")
                elif UWin.u5==1:
                    rs.set("RESULT: YOU NEED FOUR MORE LINES TO WIN")
            if np.add.reduce(wins[i])==0 and i not in SFl.sfl:
                SFl.sfl=np.append(SFl.sfl,int(i))
                SWin.s5+=1
                if SWin.s5==5:
                    srs.set("SYSTEM RESULT: BINGO SYSTEM HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif SWin.s5==4:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS ONE MORE LINE TO WIN")
                elif SWin.s5==3:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS TWO MORE LINES TO WIN")
                elif SWin.s5==2:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS THREE MORE LINES TO WIN")
                elif SWin.s5==1:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS FOUR MORE LINES TO WIN")
            if wins[0][0]==0 and wins[1][1]==0 and wins[2][2]==0 and wins[3][3]==0 and wins[4][4]==0 and 7 not in SFl.sfl:
                SWin.s5+=1
                SFl.sfl=np.append(SFl.sfl,7)
                if SWin.s5==5:
                    srs.set("SYSTEM RESULT: BINGO SYSTEM HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif SWin.s5==4:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS ONE MORE LINE TO WIN")
                elif SWin.s5==3:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS TWO MORE LINES TO WIN")
                elif SWin.s5==2:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS THREE MORE LINES TO WIN")
                elif SWin.s5==1:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS FOUR MORE LINES TO WIN")
            if wins[0][4]==0 and wins[1][3]==0 and wins[2][2]==0 and wins[3][1]==0 and wins[4][0]==0 and 8 not in SFl.sfl:
                SWin.s5+=1
                SFl.sfl=np.append(SFl.sfl,8)
                if SWin.s5==5:
                    srs.set("SYSTEM RESULT: BINGO SYSTEM HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif SWin.s5==4:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS ONE MORE LINE TO WIN")
                elif SWin.s5==3:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS TWO MORE LINES TO WIN")
                elif SWin.s5==2:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS THREE MORE LINES TO WIN")
                elif SWin.s5==1:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS FOUR MORE LINES TO WIN")
            if wins[0][i]==0 and wins[1][i]==0 and wins[2][i]==0 and wins[3][i]==0 and wins[4][i]==0 and i+9 not in SFl.sfl:
                SWin.s5+=1
                SFl.sfl=np.append(SFl.sfl,int(i+9))
                if SWin.s5==5:
                    srs.set("SYSTEM RESULT: BINGO SYSTEM HAVE WON\nGAME OVER")
                    bingo.usa[bingo.usa>0]=0
                    bingo.val_upd()
                    bingo.Playagain()
                elif SWin.s5==4:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS ONE MORE LINE TO WIN")
                elif SWin.s5==3:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS TWO MORE LINES TO WIN")
                elif SWin.s5==2:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS THREE MORE LINES TO WIN")
                elif SWin.s5==1:
                    srs.set("SYSTEM RESULT: SYSTEM NEEDS FOUR MORE LINES TO WIN")
                
                    
    def val_upd():
        u1.set(bingo.usa[0])
        u2.set(bingo.usa[1])
        u3.set(bingo.usa[2])
        u4.set(bingo.usa[3])
        u5.set(bingo.usa[4])
        u6.set(bingo.usa[5])
        u7.set(bingo.usa[6])
        u8.set(bingo.usa[7])
        u9.set(bingo.usa[8])
        u10.set(bingo.usa[9])
        u11.set(bingo.usa[10])
        u12.set(bingo.usa[11])
        u13.set(bingo.usa[12])
        u14.set(bingo.usa[13])
        u15.set(bingo.usa[14])
        u16.set(bingo.usa[15])
        u17.set(bingo.usa[16])
        u18.set(bingo.usa[17])
        u19.set(bingo.usa[18])
        u20.set(bingo.usa[19])
        u21.set(bingo.usa[20])
        u22.set(bingo.usa[21])
        u23.set(bingo.usa[22])
        u24.set(bingo.usa[23])
        u25.set(bingo.usa[24])
root=tk.Tk()
root.title("BINGO")
root.geometry("1600x900")
u1=tk.StringVar()
u2=tk.StringVar()
u3=tk.StringVar()
u4=tk.StringVar()
u5=tk.StringVar()
u6=tk.StringVar()
u7=tk.StringVar()
u8=tk.StringVar()
u9=tk.StringVar()
u10=tk.StringVar()
u11=tk.StringVar()
u12=tk.StringVar()
u13=tk.StringVar()
u14=tk.StringVar()
u15=tk.StringVar()
u16=tk.StringVar()
u17=tk.StringVar()
u18=tk.StringVar()
u19=tk.StringVar()
u20=tk.StringVar()
u21=tk.StringVar()
u22=tk.StringVar()
u23=tk.StringVar()
u24=tk.StringVar()
u25=tk.StringVar()
sc=tk.StringVar()
rs=tk.StringVar()
srs=tk.StringVar()
rs.set("RESULT:")
srs.set("SYSTEM RESULT:")
sc.set("System Choice:")
frame = tk.Frame(root)
#frame.grid()
tk.Label(frame, text = "BINGO", font = ('Helvetica', 25), pady = '30', fg = 'Red').pack()
frame.pack()
frame2=tk.Frame(root)
tk.Button(frame2, text = "Generate Game Slip",bg = '#ADD8E6', padx = '25', pady = '20', command = bingo.start, height = ' 1', width = '10').pack(side = 'top', padx = '25')
frame2.pack(pady = '15')

frame3=tk.Frame(root)
choicel=tk.Label(frame3, text = "Enter your choice:", font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue').pack(side = 'left')
choice=tk.Entry(frame3, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
choice.pack(side = 'left', pady = '25', padx = '50')
tk.Button(frame3,text='OK',bg = '#ADD8E6', padx = '15', pady = '10', command =bingo.Choice, height = ' 1', width = '10').pack(side = 'top', padx = '15')
frame3.pack(pady = '15')
frame4=tk.Frame(root)
S_choice=tk.Label(frame4, textvariable =sc, font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue').pack(side = 'left')
frame4.pack(pady = '15')

def close_window():
    root.destroy()


root.mainloop()
        