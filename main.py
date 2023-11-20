from tkinter import Tk, StringVar, Button, Entry, Label
from PIL import Image, ImageTk, ImageDraw
from tkinter import filedialog


root = Tk()
root.title("Watermark")

# GLOBAL VARIABLES
WATERMARK_TEXT = StringVar()
WATERMARK_TEXT.set("")
IMAGE_PATH = None
ORIGINAL_IMAGE = None
TK_IMAGE = None


def select_image():
    global ORIGINAL_IMAGE
    global IMAGE_PATH
    global TK_IMAGE
    file_path = filedialog.askopenfilename(filetypes=[("Image", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        IMAGE_PATH = file_path
        ORIGINAL_IMAGE = Image.open(IMAGE_PATH)
        TK_IMAGE = ImageTk.PhotoImage(ORIGINAL_IMAGE)

        image_label = Label(root, image=TK_IMAGE)
        image_label.image = TK_IMAGE
        image_label.pack()


def add_watermark():
    if ORIGINAL_IMAGE != None:
        copy_image = ORIGINAL_IMAGE.copy()
        watermark_text = WATERMARK_TEXT.get()

        editing_img = ImageDraw.Draw(copy_image)

        text_axis = editing_img.textbbox((0, 0), watermark_text)
        text_width = text_axis[2] - text_axis[0]
        text_height = text_axis[3] - text_axis[1]

        position = ((copy_image.width - text_width) // 2, copy_image.height - text_height - 10)
        editing_img.text(position, watermark_text, fill="white")

        processed_image = ImageTk.PhotoImage(copy_image)
        image_label = Label(root, image=processed_image)
        image_label.image = processed_image
        image_label.pack()


open_button = Button(root, text="Select image", command=select_image)
open_button.pack(pady=10)

watermark_entry = Entry(root, textvariable=WATERMARK_TEXT, width=30)
watermark_entry.pack(pady=5)

watermark_button = Button(root, text="Add Watermark", command=add_watermark)
watermark_button.pack(pady=10)


root.mainloop()
