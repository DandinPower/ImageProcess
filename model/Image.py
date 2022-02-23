import cv2
import numpy as np
Jpg = ".jpg"
Png = ".png"
Bmp = ".bmp"


def isGreen(R, G, B):
    adjust = 35
    if (G >= R and G >= B):
        if (G-R > adjust and G-B > adjust):
            return True
    return False


def isBlue(R, G, B):
    adjust = 35
    if (R >= G and R >= B):
        if (R-G > adjust and R-B > adjust):
            if (G < 90 and B < 90):
                return True
    return False


def isTrue(R, G, B):
    if (R >= 30 and R <= 50 and B >= 30 and B <= 50 and G >= 30 and G <= 50):
        return True
    return False

def changecolor(image):
    height, width, ret = image.shape
    for i in range(height):
        for j in range(width):
            if (isGreen(image[i, j][0], image[i, j][1], image[i, j][2])):
                image[i, j] = (0, 255, 0)
    return image


def Cutimage(image, x, y, width, height):
    return image[y:y+height, x:x+width]


def flip(image):
    return cv2.flip(image, 1)


def resize(image, scale):
    height, width, ret = image.shape
    height *= scale
    width *= scale
    height = int(height)
    width = int(width)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def resize_xy(image, x, y):
    height = int(y)
    width = int(x)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def copy(image, image2, x, y):
    height, width, ret = image2.shape
    image[y:y+height, x:x+width] = image2[0:height, 0:width]
    return image


def drag(img, Width, Height):
    OriginHeight, OriginWidth, ret = img.shape
    img2 = np.zeros((Height, Width, 3), np.uint8)
    img2.fill(255)
    newX = Width - OriginWidth
    newY = Height - OriginHeight
    img2[newY:newY+OriginHeight, newX:newX +
         OriginWidth] = img[0:OriginHeight, 0:OriginWidth]
    return img2


def isChange(B, G, R):
    if R <= 255 and R >= 140 and G <= 240 and G >= 90 and B <= 200 and B >= 0:
        return True
    else:
        return False


orange = (20, 85, 234)
black = (56, 25, 32)
deepblue = (58, 27, 36)
pink = (230, 218,166)


def changecolor_2(image):
    height, width, ret = image.shape
    for i in range(height):
        for j in range(width):
            if (isChange(image[i, j][0], image[i, j][1], image[i, j][2])):
                image[i, j] = pink
            else:
                image[i, j] = black
    return image


def main():
    img = cv2.imread("test/0.png")
    img = changecolor_2(img)
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("finish/ig2.png", img)


if __name__ == '__main__':
    main()
