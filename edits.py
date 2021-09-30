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
    

def edge_detection(imgName: str, threshold: int) -> images.Image:
    white = (255, 255, 255)
    black = (0, 0, 0)
    img = images.Image(imgName)

    def brightness_diff(pixel1, pixel2):
        r1, g1, b1 = pixel1
        lum1 = 0.299 * r1 + 0.587 * g1 + 0.114 * b1
        r2, g2, b2 = pixel2
        lum2 = 0.299 * r2 + 0.587 * g2 + 0.114 * b2
    
        return abs(lum1 - lum2)

    for x in range(1, img.getWidth()):
        for y in range(img.getHeight() - 1):
            current_pixel = img.getPixel(x, y)
            left_pixel = img.getPixel(x - 1 , y)
            bottom_pixel = img.getPixel(x, y + 1)

            if brightness_diff(current_pixel, left_pixel) > threshold or\
                    brightness_diff(current_pixel, bottom_pixel) > threshold:
                        img.setPixel(x, y, black)
            else:
                img.setPixel(x, y, white)

    return img



if __name__ == "__main__":
    #imgName = "./imageFiles/apple3.gif"
    img3 = "./imageFiles/tiger.gif"

    #img1 = color_filter(imgName, (199, 55, 47), 150)
    #img2 = grayscale(imgName)
    img3 = edge_detection(imgName=img3, threshold=200)


    #img1.draw()
    #img2.draw()
    img3.draw()




