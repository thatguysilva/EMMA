from PIL import Image
import tkinter as tk
from tkinter import Text, Entry, Button, DISABLED, constants, END, NORMAL
from chat import get_response, bot_name
from tkinter import messagebox

root = tk.Tk()
root.iconbitmap(default='Blank.ico')
root.geometry('300x600')
root.resizable(False, False)
root.title("                               EMMA")
file="mandala.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]



count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(20,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

gif_label = tk.Label(root,image="")
gif_label.pack()


animation(count)



def _on_enter_pressed(event):
    msg = msg_entry.get()
    _insert_message(msg, "You")



def _insert_message(msg, sender):
    if not msg:
        return

    msg_entry.delete(0, END)
    msg1 = f"{sender}: {msg}\n\n"
    text_widget.configure(state = NORMAL)
    text_widget.insert(END, msg1)
    text_widget.configure(state=DISABLED)

    msg2 = f"{bot_name}: {get_response(msg)}\n\n"
    text_widget.configure(state = NORMAL)
    text_widget.insert(END, msg2)
    text_widget.configure(state=DISABLED)
    text_widget.see(END)

text_widget = Text(root, bg="black", fg="white", padx=5, pady=10)
text_widget.insert(END, "EMMA: Who are you? \n \n")
text_widget.place(width=300,height=230, y=350)
text_widget.configure(cursor="arrow", state=DISABLED)

msg_entry = Entry(root, bg="black", fg="white")
msg_entry.place(width=260, height=30, y=570)
msg_entry.focus()
msg_entry.bind("<Return>", _on_enter_pressed)

send_button = Button(root, text="Send", font=("Helvetica",8), bg="black",fg="white", command=lambda: _on_enter_pressed(None))
send_button.place(width=40,height=30,x=260,y=570)


root.mainloop()
