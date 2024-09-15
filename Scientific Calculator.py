from tkinter import *
import tkinter.messagebox, math

#canvas
master = Tk()
master.title("Scientific Calculator")
#master.iconbitmap('E:\project\calculator.ico')
master.configure(background="#FFFECB")
master.resizable(width=False, height=False)
master.geometry("405x565")

#calculator
def simple():
    master.resizable(width=False, height=False)
    master.geometry("405x565")
def Scientific():
    master.geometry("740x565")
    master.resizable(width=False, height=False)
def Exit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit ?")
    if iExit>0:
        master.destroy()
        return

#menu bar
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Standard", font=("Helvetica", 10, "bold"), command=simple) 
filemenu.add_command(label="Scientific", font=("Helvetica", 10, "bold"), command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Close", font=("Helvetica", 10, "bold"), command=Exit)
menubar.add_cascade(label="File",menu=filemenu)
master.config(menu=menubar)

#entry
entry=Entry(master,font=("HELVICTA", 20, "bold"), fg='PURPLE', bg='#B4C5E4', bd=10, width=25, justify=RIGHT)
entry.grid(columnspan=4, padx=5, pady=5)
entry.bind("<Return>", lambda event: click("="))


#label
lblDisplay = Label(master, text = "Scientific Calculator",
                   font=('Helvetica',25,'bold'),
                   bg='#FFFECB',fg='#151E3F') 
lblDisplay.grid(column =4, row = 0, columnspan = 3)

# buttons
button_list = ["CE","C", "(", ")","rad","deg", "π", 
               "7", "8", "9",  chr(247),"Sinθ", "Cosθ", "Tanθ",
               "4", "5", "6", "x","sin\u207b\u00b9", "cos\u207b\u00b9", "tan\u207b\u00b9",
               "1", "2", "3", "+","x\u00B2", "x\u02b8", "√",
               ".", "0", "=", "-","log10", "ln", "x!"]

#display button
r = 1
c = 0
for i in button_list:    
    button = Button(master, text= i , font = ('Helvicta 17 bold'),fg='PURPLE', bg='#B4C5E4',
                    padx=22, pady=22, bd = 3, width= 2, height= 1,
                    command=lambda button = i:click(button))
    button.grid(row = r, column=c,padx = 4, pady = 4)
    c += 1
    if c > 6:
        r += 1
        c = 0
but_rad =Button(master, text= "rad" , font = ('Helvicta 17 bold'),fg='red', bg='#B4C5E4',
                    padx=22, pady=22, bd = 3,  width= 2, height= 1,
                    command=lambda button = "rad":click(button))

but_rad.grid(row = 1, column= 4,padx = 4, pady = 4)
but_deg =Button(master, text= "deg" , font = ('Helvicta 17 bold'),fg='red', bg='#B4C5E4',
                    padx=22, pady=22, bd = 3,  width= 2, height= 1,
                    command=lambda button = "deg":click(button))

#trig
m=0
def sin_conv(e):
    global m
    if m == 0:     
        return math.sin(e)  
    if m == 1:
        return math.sin(math.pi/180*e)
def cos_conv(e):
    global m
    if m == 0:     
        return math.cos(e)  
    if m == 1:
        return math.cos(math.pi/180*e)
def tan_conv(e):
    global m
    if m == 0:       
        return math.tan(e)  
    if m == 1:
        return math.tan(math.pi/180*e)

def sini_conv(e):
    global m
    if m == 0:       
        return math.asin(e)  
    if m == 1:
        return math.asin(e)*(180/math.pi)
def cosi_conv(e):
    global m
    if m == 0:       
        return math.acos(e)  
    if m == 1:
        return math.acos(e)*(180/math.pi)
def tani_conv(e):
    global m
    if m == 0:       
        return math.atan(e)  
    if m == 1:
        return math.atan(e)*(180/math.pi)

#function
fact, log, ln, sqrt = math.factorial, math.log10, math.log, math.sqrt
sin, cos, tan = sin_conv, cos_conv, tan_conv
asin, acos, atan = sini_conv, cosi_conv, tani_conv
π = math.pi

#calculator
def click(val):
    e = entry.get()  # getting the value
    ans = " "
    global m
    try:
        if val == "C":
            e = e[0:len(e) - 1]
            entry.delete(0, "end")
            entry.insert(0, e)
            return
        elif val == "CE":
            entry.delete(0, "end")

            
        elif val == chr(247):
            entry.insert("end", "/")
            return
        elif val == "x":
            entry.insert("end", "*")
            return
        elif val == "π":
            entry.insert("end", "π")
            return

            
        elif val == "x!":
            entry.insert("end", "fact(")
            return
            
        elif val == "x\u00B2":
            entry.insert("end", "**2")
            return
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return    
        elif val == "√":
            entry.insert("end", "sqrt(")
            return    


        elif val == "log10":
            entry.insert("end", "log(")
            return
        elif val == "    ln   ":
            entry.insert("end", "ln(")
            return


        elif val == "rad":
            m=0
            print("RAD")
            but_deg.grid_remove()
            but_rad.grid(row = 1, column= 4,padx = 4, pady = 4)
        elif val == "deg":
            m=1
            print("DEG")
            but_rad.grid_remove()
            but_deg.grid(row = 1, column= 5,padx = 4, pady = 4)


        elif val == "Sinθ":
            entry.insert("end", "sin(")
            return       
        elif val == "Cosθ":
            entry.insert("end", "cos(")
            return
        elif val == "Tanθ":
            entry.insert("end", "tan(")
            return
        elif val == "sin\u207b\u00b9":
            entry.insert("end", "asin(")
            return
        elif val == "cos\u207b\u00b9":
            entry.insert("end", "acos(")
            return
        elif val == "tan\u207b\u00b9":
            entry.insert("end", "atan(")
            return

        
        elif val == "=":
            try:
                ans = round(eval(e), 4)
                print("Answer is :", ans)
            except Exception:
                ans = "Error"
        else:
            entry.insert("end", val)
            return
        
        entry.delete(0, "end")
        entry.insert(0, ans)
    except SyntaxError:
        pass

master.mainloop()