import tkinter as tk
from PIL import Image, ImageTk
import os, sys, time

class Frame():
    def __init__(self):
        self.root = tk.Tk()
        imageFile = ""
        self.images = []
        for a in range(1, 4):
            imageFile = os.path.expanduser('~/') + str(a) + ".jpg"
            self.images.append(ImageTk.PhotoImage(Image.open(imageFile)))
        self.imageindex = 0
        self.imagemax = 3
        self.changetime = 5000
        w = self.images[self.imageindex].width()
        h = self.images[self.imageindex].height()
        self.root.geometry("%dx%d+%d+%d" % (w, h, 0, 0))
        self.panel = tk.Label(self.root, image=self.images[self.imageindex])
        self.panel.pack()
        self.root.after(self.changetime, self.update_image)
        self.root.mainloop()

    def update_image(self):
        self.imageindex += 1
        if self.imageindex == self.imagemax:
            self.imageindex = 0
        self.panel.configure(image=self.images[self.imageindex])
        self.root.after(self.changetime, self.update_image)

def main():
    app = Frame()

if __name__ == '__main__':
    main()
    
