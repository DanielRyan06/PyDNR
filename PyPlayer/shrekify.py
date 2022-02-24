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

    generate_button = ttk.Button(
        start,
        text='Generate My Robux',
        command=screen_2,)
    generate_button.pack(
        ipadx=150,
        ipady=40,
        expand=True)

    generate_button = ttk.Button(
        start,
        text="Exit",
        command=no_escape)
    generate_button.pack(
        ipadx=150,
        ipady=40,
        expand=True)

    start.mainloop()

main()