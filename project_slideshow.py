from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow Viewer")

#List of image path
image_paths = [
    r"C:\Users\LENOVO\Downloads\spider manv.jpeg",
    r"C:\Users\LENOVO\Downloads\download (4).jpg",
    r"C:\Users\LENOVO\Downloads\elon.jpeg",
    r"C:\Users\LENOVO\Downloads\1.jpg",

]

#Resize the images to 1080x1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3) #Display each image for 3 seconds

slideshow = cycle(photo_images)

def start_slideshows():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='play slideshow', command=start_slideshows)
play_button.pack()

root.mainloop()
