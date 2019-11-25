import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from skimage.metrics import structural_similarity
import math


def convertDecToHex(decimalNumber):
    if decimalNumber <= 15:
        return "0" + np.base_repr(decimalNumber, 16)
    else:
        return np.base_repr(decimalNumber, 16)


def image_histogram(image):
    img = cv2.imread(image, 0)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def img_ravel(image):
    img = cv2.imread(image, 0)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist, bins = np.histogram(img.ravel(), 256, [0, 256])

    return img.ravel()


def calculate_ssim(first_image, second_image):
    imageA = cv2.imread(first_image)
    imageB = cv2.imread(second_image)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # structural_similarity_index = structural_similarity(imageA, imageB, multichannel=True)
    structural_similarity_index = structural_similarity(grayA, grayB)

    print("Structural Similarity Index: {}".format(structural_similarity_index))


def generate_random_number(image, random):
    im = Image.open(image)
    random_numbers = np.empty((im.size[0], im.size[1], 6), dtype=int)

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            for k in range(6):
                random_numbers[i][j][k] = random.randint(0, 15)

    return random_numbers


def psnr(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    psnr = cv2.PSNR(img1, img2, 255)

    img1 = img1.astype(np.float64) / 255.
    img2 = img2.astype(np.float64) / 255.

    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
         print("Same Image")
    else:
        print(10 * math.log10(1. / mse))

    return psnr
