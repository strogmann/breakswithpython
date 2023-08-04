import tkinter as tk

window = tk.Tk()

window.geometry("800x600")
window.title("TK Test")

label1 = tk.Label(window, text="Salami Alayycum", font=('Serif', 16))
label1.pack(padx=10, pady=30)

textbox1 = tk.Text(window, height=1, font=('Serif', 16))
textbox1.pack(padx=10, pady=30)

entry1 = tk.Entry(window)
entry1.pack()
#if entry1 == "salami":
    #label1 = tk.Label(window, text="How the fuck you did you guess the word??? Hacker???", font=('Serif', 16))

window.mainloop()
