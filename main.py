from tkinter import Tk, StringVar, Button, Entry


root = Tk()
root.title("Watermark")

# GLOBAL VARIABLES
WATERMARK_TEXT = StringVar()
WATERMARK_TEXT.set("")

open_button = Button(root, text="Select image")
open_button.pack(pady=10)

watermark_entry = Entry(root, textvariable=WATERMARK_TEXT, width=30)
watermark_entry.pack(pady=5)

watermark_button = Button(root, text="Add Watermark")
watermark_button.pack(pady=10)


root.mainloop()
