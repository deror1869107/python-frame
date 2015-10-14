import tkinter as tk
from PIL import Image, ImageTk
import os, sys, time

class Frame():
    def __init__(self):
        self.root = tk.Tk()
        image_file = ""
        self.images = []
        self.image_files = []
        self.maxsize = (1024, 1024)
        include_extension = ['.jpg', '.png']
        directory = os.path.expanduser('~/') + 'pics/'
        for image_file in os.listdir(directory):
            #imageFile = "~/pics/" + str(a) + ".jpg"
            if os.path.splitext(image_file)[1] not in include_extension:
                continue
            self.image_files.append(directory + image_file)
        photo = Image.open(self.image_files[0])
        photo.thumbnail(self.maxsize)
        self.image = ImageTk.PhotoImage(photo)
        
        #self.images.append(ImageTk.PhotoImage(photo))
        self.image_index = 0
        self.change_time = 15000
        w = self.image.width()
        h = self.image.height()
        self.root.geometry('{width}x{height}'.format(width=w, height=h))
        self.panel = tk.Label(self.root, image=self.image)
        self.panel.pack()
        self.root.after(self.change_time, self.update_image)
        self.root.mainloop()
    
    def update_image(self):
        self.image.__del__()
        self.image_index += 1
        self.image_index %= len(self.image_files)
        photo = Image.open(self.image_files[self.image_index])
        photo.thumbnail(self.maxsize)
        self.image = ImageTk.PhotoImage(photo) #What the F.....
        w = self.image.width()
        h = self.image.height()
        self.root.geometry('{width}x{height}'.format(width=w, height=h))
        self.panel.configure(image=self.image)
        self.root.after(self.change_time, self.update_image)

def main():
    app = Frame()

if __name__ == '__main__':
    main()

