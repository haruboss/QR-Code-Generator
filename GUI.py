from tkinter import *
import pyqrcode
import png
import PIL
from PIL import Image
from PIL import ImageTk

root = Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + '.png'
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(
    Image.open(file_name)
    )
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,400, window=image_label)

# creating a canvas screen
canvas = Canvas(root, width=400, height=600)
canvas.pack()

# adding QR label 
app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200,50, window=app_label)

# adding link label
name_label = Label(root, text='Link Name')
link_label = Label(root, text='Link')
# adding label to window
canvas.create_window(200,100, window=name_label)
canvas.create_window(200,160, window=link_label)

# getting name and link by input
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200,130, window=name_entry)
canvas.create_window(200,180, window=link_entry)

# adding button for generating qr code
button = Button(text="Generate QR code", command=generate) # calling generate function to creating QR code
canvas.create_window(200,230, window=button)

root.mainloop()