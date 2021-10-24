import math
class Color:
    """
    Class for handling different color types currently handles RGB and HSV 
    usage
    >>> color = Color()
    >>> color.fromHSV(150, 50, 40) # to create color form HSV
    >>> print(color) # this will print the RGB value
    """
    __slots__ = ("red", "green", "blue")
    def __init__(self):
        self.red = self.green = self.blue = 0

    def fromRGB(self, red : int, green : int, blue : int):
        self.red = red
        self.green = green
        self.blue = blue

    def fromHSV(self , hue : float, saturation : float, value : float):
        """
        convert HSV to RGB and store it in the object
        """
        s = saturation / 100
        v = value / 100
        chroma = s * v
        x = chroma * (1 - math.fabs( ((hue / 60) % 2 ) - 1))
        m = v - chroma
        r = g = b = 0
        if hue >= 0 and hue < 60:
            r, g, b = (x, chroma, 0)
        elif hue >= 120 and hue < 180:
            r, g, b = (0 , chroma, x)
        elif hue >= 180 and hue < 240:
            r, g, b = (0, x, chroma)
        elif hue >= 240 and hue < 300:
            r, g, b = (x, 0, chroma)
        else:
            r, g, b = (chroma, 0 , x)

        self.red = int((r + m) * 255)
        self.green = int((g + m ) * 255)
        self.blue = int((b + m) * 255)



    def toRGB(self) : 
        return (self.red, self.blue, self.green)

    def toHSV(self):
        r = self.red / 255
        g = self.green / 255
        b = self.blue / 255
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin
        value = cmax
        saturation = delta / cmax if cmax != 0 else 0
        hue = 0
        if cmax == r:
            hue = 60 * ( ((g - b)/ delta )  % 6)
        elif cmax == g:
            hue = 60 * (((b - r) / delta) + 2)
        else:
            hue = 60 * (((r - g)/ delta) + 4)
        return (hue, saturation * 100, value * 100)

    def __str__(self):
        return f"({self.red}, {self.green}, {self.blue})"

if __name__ == "__main__":
    color = Color()
    color.fromHSV(150, 50,40)
    print(color)
    print(color.toHSV())
