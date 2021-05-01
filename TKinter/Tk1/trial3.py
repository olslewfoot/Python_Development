import tkinter as tk

window=tk.Tk()
text_box=tk.Text()

text_box.pack()
content=text_box.get("1.0",tk.END)

window.mainloop()