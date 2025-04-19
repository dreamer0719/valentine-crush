import tkinter as tk
import pygame
from tkinter import ttk
import random
from PIL import Image, ImageTk

## Default
root = tk.Tk()
root.configure(bg='white')
root.title("From Kim :3")
root.geometry('300x250')
root.resizable(False, False)
def show_frame(frame_to_show):
    for frame in [a_frame, a_n_frame, b_frame, b_n_frame, c_frame, c_n_frame,
                  d_frame, d_n_frame, e_frame, f_frame, g_frame, h_frame,
                  main_frame, second_frame]:
        frame.pack_forget()
    frame_to_show.pack()

# Styles:
hi = ('Helvetica', 12,'bold')
### Screen breathing(a):
def a_y():
    show_frame(b_frame)
def a_n():
    show_frame(a_n_frame)

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


#a_n frame (breathing no)
def a_return():
    show_frame(a_frame)

a_n_frame = tk.Frame(root, bg='white',width=300, height=250)
a_n_label = tk.Label(a_n_frame, text='This you?', font=hi, bg='white', bd=0, relief ='flat')
a_n_label.pack(pady=7)

a_n_image = Image.open('./c/cat_dying.png')
resize_a_n_img = a_n_image.resize((165,165))
a_n_img = ImageTk.PhotoImage(resize_a_n_img)
tk.Label(a_n_frame, image=a_n_img, bg='white',bd=0,relief = 'flat').pack(anchor='center')

next_btn = tk.Button(a_n_frame, text = 'Return', command = a_return)
next_btn.pack(pady=8)

a_n_frame.pack_propagate(False)
a_n_frame.pack()


### Screen gay(b):
# No I'm not gay is for yes
def b_y():
    show_frame(c_frame)
def b_n():
    show_frame(b_n_frame)

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


#b_n frame (gay yes)
def b_return():
    show_frame(b_frame)

b_n_frame = tk.Frame(root, bg='white',width=300, height=250)
b_n_label = tk.Label(b_n_frame, text='Dawg my bad gang', font=hi, bg='white', bd=0, relief ='flat')
b_n_label.pack(pady=7)

b_n_image = Image.open('./c/cat_dying_2.png')
resize_b_n_img = b_n_image.resize((165,165))
b_n_img = ImageTk.PhotoImage(resize_b_n_img)
tk.Label(b_n_frame, image=b_n_img, bg='white',bd=0,relief = 'flat').pack(anchor='center')

next_btn = tk.Button(b_n_frame, text = 'Return', command = b_return)
next_btn.pack(pady=8)

b_n_frame.pack_propagate(False)
b_n_frame.pack()


### Screen guy(c):
def c_y():
    show_frame(d_frame)
def c_n():
    show_frame(c_n_frame)

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


#c_n frame (guy no)
def c_return():
    show_frame(c_frame)
c_n_frame = tk.Frame(root, bg='white',width=300, height=250)
c_n_label = tk.Label(c_n_frame, text="Don't worry milady, we can go to \nscissor city together", font=hi, bg='white', bd=0, relief ='flat')
c_n_label.pack(pady=7)

c_n_image = Image.open('./c/freaky_cat.png')
resize_c_n_img = c_n_image.resize((150,150))
c_n_img = ImageTk.PhotoImage(resize_c_n_img)
tk.Label(c_n_frame, image=c_n_img, bg='white',bd=0,relief = 'flat').pack(anchor='center')

next_btn = tk.Button(c_n_frame, text = 'Return', command = c_return)
next_btn.pack(pady=8)

c_n_frame.pack_propagate(False)
c_n_frame.pack()


### Screen funny(d):
def d_y():
    show_frame(e_frame)
def d_n():
    show_frame(d_n_frame)

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


#d_n frame (funny no)
def d_return():
    show_frame(d_frame)

d_n_frame = tk.Frame(root, bg='white',width=300, height=250)
d_n_label = tk.Label(d_n_frame, text="Ouch, that's hurt :(", font=hi, bg='white', bd=0, relief ='flat')
d_n_label.pack(pady=7)

d_n_image = Image.open('./c/sad_cat.png')
resize_d_n_img = d_n_image.resize((165,165))
d_n_img = ImageTk.PhotoImage(resize_d_n_img)
tk.Label(d_n_frame, image=d_n_img, bg='white',bd=0,relief = 'flat').pack(anchor='center')

next_btn = tk.Button(d_n_frame, text = 'Return', command = d_return)
next_btn.pack(pady=8)

d_n_frame.pack_propagate(False)
d_n_frame.pack()

### Screen microwave(e):
def process_text(event):
    root.after(250)
    show_frame(f_frame)

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
    show_frame(g_frame)

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
    root.after(350,lambda: show_frame(h_frame))

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
    max_value = 100
    total_duration = 3200
    steps = 100
    interval = total_duration // steps
    increment = max_value/ steps

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
    root.after(2500, lambda: [show_frame(main_frame), 
                              fade_in_label(main_label,'#FFFFFF', '#FA5858')])

def play_sound():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('./sound.mp3')
    sound.play(loops=-1, fade_ms=3500)

h_frame = tk.Frame(root, bg='white', width=300, height=250)
h_label = tk.Label(h_frame, text = "Process to calculate points \nbased on your provided answers?", 
                   font=hi,bg='white',bd=0, relief = 'flat')
h_label.pack(pady=10)

Yes_btn = tk.Button(h_frame, text = 'Calculate', command = start_progress)
Yes_btn.pack(pady=10)

Yes_a_btn = tk.Button(h_frame, text= 'See your result?',command=lambda:[h_next(), play_sound()])

h_frame.pack_propagate(False)
h_frame.pack()


### Last Screen (main_frame):
def fade_in_label(label, start_color, end_color, steps=40, delay=75):
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#') #Remove # infront
        return tuple(int(hex_color[i:i+2],16) for i in (0,2,4))
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    def interpolate(step):
        new_color = tuple(int(start + (end-start)*step/steps)
                          for start, end in zip(start_rgb, end_rgb))
        label.config(fg=rgb_to_hex(new_color))
        if step<steps:
            root.after(delay, interpolate, step + 1)

    interpolate(0)

def clicked_yes():
    show_frame(second_frame)
    
def clicked_no(event=None):
    root.after(100,move_no_btn)

def move_no_btn():
    x=random.randint(0,230) 
    y=random.randint(50,220)
    No_btn.place(x=x,y=y)


main_frame = tk.Frame(root, bg='white', width=300, height=250)


main_label = tk.Label(main_frame, text = "Will you be my boyfriend?", font=('Helvetica',12,'bold'),bg='white',
                      bd=0,relief='flat',fg='#FFFFFF')
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