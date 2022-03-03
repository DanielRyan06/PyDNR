from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
import tkinter.font as font
from tkinter.messagebox import showerror, showwarning, showinfo

def screen_2():
    window = tk.Tk()
    window.geometry('800x550')
    window.resizable(True, True)
    window.title("Generating...")

def no_escape():
    print("No escape")
    title = "Error"
    message = "error: can't exit because your a fucking retard. why would you think it was a good idea to run a file named Free Robux Generator."
    showerror(title, message)

def main():
    start = tk.Tk()
    start.geometry('600x400')
    start.resizable(False, False)
    start.title("Free Robux Generator")
    start.iconbitmap("./assets/icon.ico")
    start.attributes('-topmost', 1)
    start.configure(bg='black')

    #Background image of start
    bg = PhotoImage(file="./assets/start.png")
    my_label = Label(start, image=bg)
    my_label.place(x=0,y=0, relwidth=1, relheight=1)
    
    #Generate button of start
    generate_button = ttk.Button(
        start,
        text="Generate My Robux",
        command=screen_2,)
    generate_button.pack(
        ipadx=30,
        ipady=20,
        expand=True)
    
    #Exit Button of start
    exit_icon = tk.PhotoImage(file='./assets/exit.png')
    generate_button = ttk.Button(
        start,
        image=exit_icon,
        command=no_escape)
    generate_button.pack(
        ipadx=0,
        ipady=0,
        expand=True)

    start.mainloop()

main()
