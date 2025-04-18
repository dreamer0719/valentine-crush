import tkinter as tk
import random
from PIL import Image, ImageTk

def clicked_yes():
    main_frame.pack_forget()
    second_frame.pack()
    
def clicked_no(event=None):
    root.after(100,move_no_btn)

def move_no_btn():
    x=random.randint(0,230) 
    y=random.randint(180,220)
    No_btn.place(x=x,y=y)
    


root = tk.Tk()
root.configure(bg='white')
root.title("From Kim :3")
root.geometry('300x250')

#the first screen
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




root.resizable(False, False)
root.mainloop()



