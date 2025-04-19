import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import n

## Default
root = tk.Tk()
root.configure(bg='white')
root.title("From Kim :3")
root.geometry('300x250')
root.resizable(False, False)
# Styles:
hi = ('Helvetica', 12,'bold')
### Screen breathing(a):
def a_y():
    a_frame.pack_forget()
    b_frame.pack()
def a_n():
    a_frame.pack_forget()
    a_n_frame.pack()

a_frame = tk.Frame(root, bg='white', width=300, height=250)
a_label = tk.Label(a_frame, text = "Are you breathing?", font=hi,bg='white',bd=0, relief = 'flat')
a_label.pack(pady=7)

a_image = Image.open('./c/cat_1.png')
resize_a_img = a_image.resize((165,165))
a_img = ImageTk.PhotoImage(resize_a_img)
tk.Label(a_frame, image=a_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

Yes_btn = tk.Button(a_frame, text = 'Yes', command = a_y)
No_btn = tk.Button(a_frame, text= 'No', command=a_n)
Yes_btn.place(x=70, y=205)
No_btn.place(x=200,y=205)

a_frame.pack_propagate(False)
a_frame.pack()


### Screen gay(b):
# No I'm not gay is for yes
def b_y():
    b_frame.pack_forget()
    c_frame.pack()
def b_n():
    b_frame.pack_forget()
    b_n_frame.pack()

b_frame = tk.Frame(root, bg='white', width=300, height=250)
b_label = tk.Label(b_frame, text = "Are you gay?", font=hi,bg='white',bd=0, relief = 'flat')
b_label.pack(pady=7)

b_image = Image.open('./c/cat_rainbow.png')
resize_b_img = b_image.resize((165,165))
b_img = ImageTk.PhotoImage(resize_b_img)
tk.Label(b_frame, image=b_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

Yes_btn = tk.Button(b_frame, text = 'Yes', command = b_n)
No_btn = tk.Button(b_frame, text= 'No', command=b_y)
Yes_btn.place(x=70, y=205)
No_btn.place(x=200,y=205)

b_frame.pack_propagate(False)
b_frame.pack()


### Screen guy(c):
def c_y():
    c_frame.pack_forget()
    d_frame.pack()
def c_n():
    c_frame.pack_forget()
    c_n_frame.pack()

c_frame = tk.Frame(root, bg='white', width=300, height=250)
c_label = tk.Label(c_frame, text = "Oops, I mean are you a guy?", font=hi,bg='white',bd=0, relief = 'flat')
c_label.pack(pady=7)

c_image = Image.open('./c/cat_2.png')
resize_c_img = c_image.resize((165,165))
c_img = ImageTk.PhotoImage(resize_c_img)
tk.Label(c_frame, image=c_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

Yes_btn = tk.Button(c_frame, text = 'Yes', command = c_y)
No_btn = tk.Button(c_frame, text= 'No', command=c_n)
Yes_btn.place(x=70, y=205)
No_btn.place(x=200,y=205)

c_frame.pack_propagate(False)
c_frame.pack()


### Screen funny(d):
def d_y():
    d_frame.pack_forget()
    e_frame.pack()
def d_n():
    d_frame.pack_forget()
    d_n_frame.pack()

d_frame = tk.Frame(root, bg='white', width=300, height=250)
d_label = tk.Label(d_frame, text = "Do you think I'm funny?", font=hi,bg='white',bd=0, relief = 'flat')
d_label.pack(pady=7)

d_image = Image.open('./c/cat_clown.png')
resize_d_img = d_image.resize((165,165))
d_img = ImageTk.PhotoImage(resize_d_img)
tk.Label(d_frame, image=d_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

Yes_btn = tk.Button(d_frame, text = 'Yes', command = d_y)
No_btn = tk.Button(d_frame, text= 'No', command=d_n)
Yes_btn.place(x=70, y=205)
No_btn.place(x=200,y=205)

d_frame.pack_propagate(False)
d_frame.pack()


### Screen microwave(e):
def process_text(event):
    root.after(250)
    e_frame.pack_forget()
    f_frame.pack()

e_frame = tk.Frame(root, bg='white', width=300, height=250)
e_label = tk.Label(e_frame, text = "What's your microwave brand?", font=hi,bg='white',bd=0, relief = 'flat')
e_label.pack(pady=7)

e_image = Image.open('./c/cat_mcro.png')
resize_e_img = e_image.resize((165,165))
e_img = ImageTk.PhotoImage(resize_e_img)
tk.Label(e_frame, image=e_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

mcro = tk.Entry(e_frame, bd=2)
mcro.pack(pady=8)
mcro.bind("<Return>", process_text)

e_frame.pack_propagate(False)
e_frame.pack()


### Screen lovely(f):
def f_y():
    f_frame.pack_forget()
    g_frame.pack()

f_frame = tk.Frame(root, bg='white', width=300, height=250)
f_label = tk.Label(f_frame, text = "Lovely...", font=hi,bg='white',bd=0, relief = 'flat')
f_label.pack(pady=7)

f_image = Image.open('./c/cat_holding_fl.png')
resize_f_img = f_image.resize((165,165))
f_img = ImageTk.PhotoImage(resize_f_img)
tk.Label(f_frame, image=f_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

Yes_btn = tk.Button(f_frame, text = 'Next', command = f_y)
Yes_btn.pack(pady=8)

f_frame.pack_propagate(False)
f_frame.pack()


### Screen compliment(g):
def g_y():
    g_frame.pack_forget()
    h_frame.pack()

g_frame = tk.Frame(root, bg='white', width=300, height=250)
g_label = tk.Label(g_frame, text = "Your laryngeal prominence: 10/10", font=hi,bg='white',bd=0, relief = 'flat')
g_label.pack()

g_image = Image.open('./c/adam.png')
resize_g_img = g_image.resize((210,210))
g_img = ImageTk.PhotoImage(resize_g_img)
tk.Label(g_frame, image=g_img, bg='white', bd=0, relief = 'flat').pack(anchor='center')

Yes_btn = tk.Button(g_frame, text = 'Uhh... thanks?', command = g_y)
Yes_btn.place(x=100, y=205)

g_frame.pack_propagate(False)
g_frame.pack()


### Screen checking(h):
def start_progress():
    Yes_btn.pack_forget()

    progress = ttk.Progressbar(h_frame, orient='horizontal', length =250, mode = 'determinate' )
    progress["value"] = 0
    max_value = 500
    interval = 50
    increment = max_value/(500/interval)

    def step():
        global current_value
        current_value = progress['value']
        if current_value < max_value:
            progress['value'] = current_value + increment
            root.after(interval, step)
        else:
            progress['value'] = max_value
            Yes_a_btn.pack(pady=10)

    step()
    progress.pack(pady=10)
    

def h_next():
    h_frame.pack_forget()
    main_frame.pack()


h_frame = tk.Frame(root, bg='white', width=300, height=250)
h_label = tk.Label(h_frame, text = "Process to calculate points \nbased on your provided answers?", 
                   font=hi,bg='white',bd=0, relief = 'flat')
h_label.pack(pady=10)

Yes_btn = tk.Button(h_frame, text = 'Calculate', command = start_progress)
Yes_btn.pack(pady=10)

Yes_a_btn = tk.Button(h_frame, text= 'See your result?',command=h_next)

h_frame.pack_propagate(False)
h_frame.pack()


### Screen Last:
def clicked_yes():
    main_frame.pack_forget()
    second_frame.pack()
    
def clicked_no(event=None):
    root.after(100,move_no_btn)

def move_no_btn():
    x=random.randint(0,230) 
    y=random.randint(50,220)
    No_btn.place(x=x,y=y)

main_frame = tk.Frame(root, bg='white', width=300, height=250)

main_label = tk.Label(main_frame, text = "Will you be my boyfriend?", font=('Helvetica',12,'bold'),bg='white',
                      bd=0,relief='flat',fg='#FA5858')
main_label.pack(pady=7)

image = Image.open("./sweet.png")
resize_img = image.resize((190,190))
img = ImageTk.PhotoImage(resize_img)
tk.Label(main_frame, image=img, bg='white', bd=0, relief = 'flat').place(x=50,y=26)


Yes_btn = tk.Button(main_frame, bg='#F8E0E0', text = 'Yes', command = clicked_yes)
No_btn = tk.Button(main_frame, bg='#F8E0E0', text= 'No')
No_btn.bind('<Enter>',clicked_no)


Yes_btn.place(x=70, y=205)
No_btn.place(x=200,y=205)

main_frame.pack_propagate(False)
main_frame.pack()

#The second screen (yes screen)
second_frame = tk.Frame(root, bg='white', width=300, height=250)
second_label = tk.Label(second_frame, text='Yippe!!!', font=('Helvetica', 12, 'bold'),bg='white',
                        bd=0, relief='flat', fg='#FA5858')
second_label.pack(pady= 7)

image_second = Image.open('./sweet_yes.png')
resize_simg = image_second.resize((250,250))
second_img = ImageTk.PhotoImage(resize_simg)
tk.Label(second_frame, image=second_img, bg='white', bd=0, relief='flat').pack()




root.mainloop()



