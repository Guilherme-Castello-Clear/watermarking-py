from tkinter import Tk, StringVar, Button, Entry, Label
from tkinter import filedialog
from PIL import Image, ImageTk


root = Tk()
root.title("Watermark")

# GLOBAL VARIABLES
WATERMARK_TEXT = StringVar()
WATERMARK_TEXT.set("")


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image_path = file_path
        original_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(original_image)
        
        image_label = Label(root, image=tk_image)
        image_label.image = tk_image
        image_label.pack()


open_button = Button(root, text="Select image", command=select_image)
open_button.pack(pady=10)

watermark_entry = Entry(root, textvariable=WATERMARK_TEXT, width=30)
watermark_entry.pack(pady=5)

watermark_button = Button(root, text="Add Watermark")
watermark_button.pack(pady=10)


root.mainloop()
