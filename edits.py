import images
import functools

def grayscale(imgName: str):
    img = images.Image(imgName)
    img_grey = img.clone()

    for x in range(img_grey.getWidth()):
        for y in range(img_grey.getHeight()):
            r, g, b = img_grey.getPixel(x, y)
            # since human eyes have different sensitivity towards different
            # colors hence we have to take the relative luminance proportions
            # of green, red, and blue and these are .587, .299, and .114
            # respectively. Note that these values add up to 1
            r, g, b = map(int, (0.299 * r, 0.587 * g, 0.114 * b))
            lum = (r + g + b)
            img_grey.setPixel(x,y, (lum, lum, lum))
    
    return img_grey


def color_filter(imgName: str, color: tuple[int, int, int], threshold: int):

    img = images.Image(imgName)
    def absoluteDiff(num1 , num2):
        return abs(num1 - num2)

    def isShadeOfColor(color, testColor):
        r, g, b = color
        r1, g1, b1 = testColor

        deltaR = r1 - r
        deltaG = g1 - g
        deltaB = b1 - b

        if absoluteDiff(deltaR, deltaB) < threshold and \
                absoluteDiff(deltaB, deltaG) < threshold and \
                absoluteDiff(deltaG, deltaR) < threshold:
                    return True
        else:
            return False

    def grayscale(color):
        r, g, b = color
        return 0.299 * r + 0.587 * g + 0.114 * b


    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            pixelColor = img.getPixel(x, y)

            if not isShadeOfColor(color, pixelColor):
                lum = int(grayscale(pixelColor))
                img.setPixel(x, y, (lum, lum, lum))
    return img
    

if __name__ == "__main__":
    img1Name = "./imageFiles/apple3.gif"
    #img2 = images.Image("./imageFiles/apple2.gif")

    img1 = color_filter(img1Name, (199, 55, 47), 150)
    #img2 = color_filter(img2, (199, 55, 47), 50)

    img1.draw()
    #img2.draw()




