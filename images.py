"""

images.py

Revised for Python 3.9.7, 2021.
Now, while using non GIF images imagemagick is a Dependency

This module, writtn by Kenneth Lambert, and modified by Kunal Sharma supports
simple image processing. The Image class represents either an image loaded from
a image file or a blank image.  

To instantiate an image from a file, enter

image = Image(aImageFileName)                   

To instantiate a blank image, enter

image = Image(aWidth, aHeight)

Image methods:

draw()                          Displays the image in a window 
getWidth()  -> anInt            The width in pixels
getHeight() -> anInt            The height in pixels
getPixel(x, y)  -> (r, g, b)    The RGB values of pixel at x, y
setPixel(x, y, (r, g, b))       Resets pixel at x, y to (r, g, b)
save()                          Saves the image to the current file name
save(aFileName)                 Saves the image to fileName

LICENSE: This is open-source software released under the terms of the
GPLv3 (https://github.com/Happy-Kunal/GNU-PhotoShop/blob/master/LICENSE).
"""

import tkinter
import os, os.path
tk = tkinter

_root = None

class ImageView(tk.Canvas):
    def __init__(self, image,
                 title = "New Image",
                 autoflush=False):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master,
                           width = image.getWidth(),
                           height = image.getHeight())
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.image = image
        self.height = image.getHeight()
        self.width = image.getWidth()
        self.autoflush = autoflush
        self.closed = False

    def close(self):
        """Close the window"""
        self.closed = True
        self.master.destroy()
        self.image.canvas = None
        _root.quit()

    def isClosed(self):
        return self.closed

    def getHeight(self):
        """Return the height of the window"""
        return self.height

    def getWidth(self):
        """Return the width of the window"""
        return self.width

class Image:
        
    def __init__(self, *args):
        self.canvas = None
        if len(args) == 1:
            name = args[0]
            if type(name) != str:
                raise Exception('Must be a file name')
            if name[-4:].upper() != '.GIF':
                newNameList = name.split(".")[0]
                for newName in newNameList:
                    if newName != "":
                        newName += ".gif"
                        break
                os.system(f"convert {name} {newName}")
                name = newName
            if not os.path.exists(name):
                raise Exception(f'{name} File not exists')
            self.image = tk.PhotoImage(file = name, master = _root)
            self.filename = name
            self.width = self.image.width()
            self.height = self.image.height()
        else: # arguments are width and height
            self.width, self.height = args
            self.image = tk.PhotoImage(master =_root,
                                       width = self.width,
                                       height = self.height)
            self.filename = ""
            		
    def getWidth(self):
        """Returns the width of the image in pixels"""
        return self.width

    def getHeight(self):
        """Returns the height of the image in pixels"""
        return self.height

    def getPixel(self, x, y):
        """Returns a tuple (r,g,b) with the RGB color values for pixel (x,y)
        r,g,b are in range(256)

        """
        value = self.image.get(x, y)
        if type(value) == int:
            return (value, value, value)
        elif type(value) == tuple:
            return value
        else:
            return tuple(map(int, value.split()))

    def setPixel(self, x, y, color):
        """Sets pixel (x,y) to the color given by RGB values r, g, and b.
        r,g,b should be in range(256)

        """
        self.image.put("{#%02x%02x%02x}" % color, (x, y))

    def draw(self):
        """Creates and opens a window on an image.
        The user must close the window to return control to
        the caller."""
        if not self.canvas:
            self.canvas = ImageView(self,
                                    self.filename)
        self.canvas.create_image(self.width // 2,
                                 self.height // 2,
                                 image = self.image)
        _root.mainloop()

    def save(self, filename = ""):
        """Saves the image to filename.  If no file name
        is provided, uses the image's file name if there
        is one; otherwise, simply returns.
        If the .gif extension is not present, it is added.
        """
        if filename == "":
            return
        else:
            self.filename = filename
        path, name = os.path.split(filename)
        ext = name.split(".")[-1]
        if ext != "gif":
            filename += ".gif"
            self.filename = filename
        self.image.write(self.filename, format = "gif")

    def clone(self):
        new = Image(self.width, self.height)
        new.image = self.image.copy()
        return new

    def __str__(self):
        rep = ""
        if self.filename:
            rep += ("File name: " + self.filename + "\n")
        rep += ("Width:  " + str(self.width) + \
                "\nHeight: " + str(self.height))
        return rep
    		
_root = tk.Tk()
_root.withdraw()



  

   

