import tkinter as tk
from PIL import Image, ImageTk
import os, sys, time

class Frame():
    def __init__(self):
        self.root = tk.Tk()
        image_file = ""
        self.images = []
        maxsize = (1024, 1024)
        include_extension = ['.jpg', '.png']
        directory = '/Users/sungyuanyao/pics/'
        for image_file in os.listdir(directory):
            #imageFile = "/Users/sungyuanyao/pics/" + str(a) + ".jpg"
            if os.path.splitext(image_file)[1] not in include_extension:
                continue
            photo = Image.open(directory + image_file)
            photo.thumbnail(maxsize)
            self.images.append(ImageTk.PhotoImage(photo))
        self.image_index = 0
        self.change_time = 15000
        w = self.images[self.image_index].width()
        h = self.images[self.image_index].height()
        self.root.geometry('{width}x{height}'.format(width=w, height=h))
        self.panel = tk.Label(self.root, image=self.images[self.image_index])
        self.panel.pack()
        self.root.after(self.change_time, self.update_image)
        self.root.mainloop()

    def update_image(self):
        self.image_index += 1
        self.image_index %= len(self.images)
        w = self.images[self.image_index].width()
        h = self.images[self.image_index].height()
        self.root.geometry('{width}x{height}'.format(width=w, height=h))
        self.panel.configure(image=self.images[self.image_index])
        self.root.after(self.change_time, self.update_image) 

def main():
    app = Frame()

if __name__ == '__main__':
    main()
    
