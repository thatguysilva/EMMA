from PIL import Image
import tkinter as tk
from tkinter import Text, Entry, Button, DISABLED
from chat import get_response, bot_name

root = tk.Tk()
root.geometry('300x600')
root.resizable(False, False)
root.title("                               EMMA")
file="new-solar.gif"

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


def _on_enter_pressed(root,event):
    msg = root.msg_entry.get()
    root._insert_message(msg, "You")



def _insert_message(root, msg, sender):
    if not msg:
        return

    self.msg_entry.delete(0, END)
    msg1 = f"{sender}: {msg}\n\n"
    root.text_widget.configure(state = NORMAL)
    root.text_widget.insert(END, msg1)
    root.text_widget.configure(state=DISABLED)

    msg2 = f"{bot_name}: {get_response(msg)}\n\n"
    root.text_widget.configure(state = NORMAL)
    root.text_widget.insert(END, msg2)
    root.text_widget.configure(state=DISABLED)
    root.text_widget.see(END)

text_widget = Text(root, bg="black", fg="white", padx=5, pady=10)

text_widget.place(width=300,height=200, y=350)
text_widget.configure(cursor="arrow", state=DISABLED)

msg_entry = Entry(root, bg="black", fg="white")
msg_entry.place(width=260, height=30, y=550)
msg_entry.focus()
msg_entry.bind("<Return>", _on_enter_pressed) #use this on BRO

send_button = Button(root, text="Send", font=("Helvetiva",8), bg="black",fg="white", command=lambda: root._on_enter_pressed(None))
send_button.place(width=40,height=30,x=260,y=550)


root.mainloop()
