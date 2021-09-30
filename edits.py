import images


def grayscale(fname: str):
    img = images.Image(str)
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




