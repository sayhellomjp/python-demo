from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = Label(self, text='hello world')
        self.hello_label.pack()
        self.hello_input = Entry(self)
        self.hello_input.pack()
        self.hello_btn = Button(self, text='quit', command=self.quit)
        self.hello_btn.pack()
        self.alertButton = Button(self, text='hello', command=self.tip)
        self.alertButton.pack()

    def tip(self):
        str = self.hello_input.get() or 'world'
        print(str)
        messagebox.showinfo('tips', 'hello %s' % str)

app = Application()
app.master.title('标题')
app.mainloop()