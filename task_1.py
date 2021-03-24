from tkinter import *

class TrafficLight:
    __colour = 0, 1, 2

    def running(self):
        for i in TrafficLight.__colour:
            if i == 0:
                root = Tk()
                button1 = Button(root, text='red', width=25, height=5, bg='red', fg='white', font='arial 14')
                button1.pack()
                root.after(7000, root.destroy)
                root.mainloop()
            elif i == 1:
                root = Tk()
                button1 = Button(root, text='yellow', width=25, height=5, bg='yellow', fg='white', font='arial 14')
                button1.pack()
                root.after(2000, root.destroy)
                root.mainloop()

            elif i == 2:
                root = Tk()
                button1 = Button(root, text='green', width=25, height=5, bg='green', fg='white', font='arial 14')
                button1.pack()
                root.after(5000, root.destroy)
                root.mainloop()


abc = TrafficLight()
abc.running()
