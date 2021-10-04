import images
import functools
import color

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


def rotate_hue(imgName : str, rotation : float):
    """
    Rotate the hue of an image with given radian
    @param imgName : str ( Name of the image )
    @param rotation : float (how much to rotate hue of the image (in degrees) ) 
    @return img : images.image (return the image after hue change)
    """
    img = images.Image(imgName)
    pixel = color.Color()
    for x in range(1 , img.getWidth()):
        for y in range(img.getHeight() - 1):
            # here we are getting the pixel at (x,y) coordinate and converting 
            # it into HSV value, then rotating the hue. Then converting HSV 
            # value back to RGB and putting it in the image
            pixel.red, pixel.green , pixel.blue = img.getPixel(x , y)
            hue, saturation, value = pixel.toHSV()
            hue += rotation
            pixel.fromHSV(hue, saturation, value)
            img.setPixel(x, y, pixel.toRGB())
    return img

def change_brightness(imgName : str, change : float):
    """
    change the brightness of the image with given change percentange
    @param imgName : str ( Name of the image )
    @param change : float ( percentange of brightness change )
    @return image : images.image (return the image after brightness change)
    """
    pixel = color.Color()
    img = images.Image(imgName)
    for x in range(1, img.getWidth()):
        for y in range(img.getHeight() - 1):
            pixel.red , pixel.green , pixel.blue = img.getPixel(x , y)
            pixel.red = int(min(255, pixel.red * change))
            pixel.green = int(min(255, pixel.green * change))
            pixel.blue = int(min(255, pixel.blue * change))
            img.setPixel(x, y, pixel.toRGB())
    return img


if __name__ == "__main__":
    img3 = "./imageFiles/apple3.gif"
    # img3 = "./imageFiles/tiger.gif"

    #img1 = color_filter(imgName, (199, 55, 47), 150)
    # img2 = rotate_hue(imgName, 60)
    # img3 = edge_detection(imgName=img3, threshold=200)
    img3 = change_brightness(img3, 1.1)


    #img1.draw()
    # img2.draw()
    img3.draw()




