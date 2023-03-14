from PIL import Image, ImageFont, ImageDraw
from tkinter import Tk, Button, Entry, Label, Canvas, PhotoImage
from tkinter import messagebox
from tkinter import filedialog, simpledialog


# ------------------------------------------------- App Functions -----------------------------------------------------
def watermark():
    filepath = filedialog.askopenfilename()
    new_filepath = filepath.replace("/", "//")
    img = Image.open(new_filepath)
    messagebox.showinfo(title="Image selected", message="Image hs been selected successfully.")
    new_filename = simpledialog.askstring(title="Name", prompt="Enter a new name for your image.")
    font_size = simpledialog.askinteger(title="Font-size", prompt="please provide the size with respect to your image"
                                                                  "size")
    messagebox.showinfo(title="color-choice", message="Next you are required to provide the color in RGB value please!")
    red = simpledialog.askinteger(title="Red or R value", prompt="Provide the R value in integer")
    green = simpledialog.askinteger(title="Green or G value", prompt="Provide the G value in integer")
    blue = simpledialog.askinteger(title="Blue or B value", prompt="Provide the B value in integer")
    draw = ImageDraw.Draw(img)
    text = entry_text.get()
    font = ImageFont.truetype("ArianaVioleta-dz2K.ttf", font_size)
    draw.text((img.size[0]/2, img.size[1]/2), f"{text}", fill=(red, green, blue), font=font)
    img.save(f"{new_filename}.{img.format}")
    messagebox.showinfo(title="Success", message="Image hase been water marked and saved successfully.")
    new_image = Image.open(f"{new_filename}.{img.format}")
    new_image.show()


def quit_it():
    window.destroy()


# --------------------------------------------------- UI setup --------------------------------------------------------
window = Tk()
window.title('Image Watermarking App')
window.config(padx=40, pady=40)

canvas = Canvas(width=400, height=300, highlightthickness=0)
logo = PhotoImage(file="cloudy.png")
canvas.create_text(200, 50, text="🦉 Welcome to Image Watermarking 🦉", font=('ariel', 15, 'bold'), fill="brown")
canvas.create_image(200, 170, image=logo)
canvas.grid(column=0, row=2, columnspan=4)

text_label = Label(text="Text:", font=("ariel", 15, "normal"))
text_label.grid(column=0, row=4)

entry_text = Entry(highlightbackground="brown", highlightthickness=10, width=50)
entry_text.grid(column=1, row=4)

watermark_image = Button(text="Start water-marking", font=("ariel", 12, "bold"), command=watermark, width=31)
watermark_image.grid(column=1, row=6)
ending = Button(text="Quit", font=("ariel", 12, "bold"), command=quit_it, width=31)
ending.grid(column=1, row=8)
window.mainloop()