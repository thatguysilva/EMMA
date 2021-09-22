from tkinter import *
from chat import get_response, bot_name
from PIL import Image




class chatapp:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()


    def run(self):
        self.window.mainloop()


    def _setup_main_window(self):
        self.window.title(" ")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=470, height=550, bg="black")

        head_label = Label(self.window, bg = "black", fg="white", text="E M M A", font=("Helvetica",13,"bold"), pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg="gray")
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg="black", fg="white", padx=5, pady=5)

        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.window, bg="gray", height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg="#2c3e50", fg="white")
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed) #use this on BRO

        send_button = Button(bottom_label, text="Send", font="Helvetiva", width=20, bg="gray", command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06,relwidth=0.22)

        


    def _on_enter_pressed(self,event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")



    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

        

if __name__ == "__main__":
    app = chatapp()
    app.run()
