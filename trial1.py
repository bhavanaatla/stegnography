from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x600")
root.resizable(True, True)
root.configure(bg="#2f4155")

# Global variables to hold image paths
filename = None
secret_image = None

def showimage():
    global filename, secret_image
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title="Select Image file",
                                         filetypes=(("PNG file", "*.png"),
                                                    ("JPG file", "*.jpg"),
                                                    ("All files", ".")))
    if filename:
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img
        secret_image = None  # Reset secret image when new image is opened

def Hide():
    global filename, secret_image
    message = text1.get(1.0, END).strip()
    if filename and message:
        secret_image = lsb.hide(filename, message)
        # Notify user that data has been hidden
        print("Data hidden successfully in image.")
    else:
        print("No image selected or message is empty.")

def Show():
    global filename
    if filename:
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)

def save():
    global secret_image
    if secret_image:
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG file", "*.png")])
        if save_path:
            secret_image.save(save_path)
            # Notify user that the image has been saved
            print(f"Image saved to {save_path}.")
    else:
        print("No image to save. Please hide data first.")

image_icon =PhotoImage(file="stegano.png")
root.iconphoto(False, image_icon)
logo = PhotoImage(file="stegano.png")
Label(root, image=logo, bg="#2f4155", width=340, height=100).place(x=10, y=10)
Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=280, y=20)

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=100)
lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=100)
text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=390)
Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=30, y=5)

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=390)
Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()